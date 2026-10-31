#!/usr/bin/env python3
"""Resolve every card referenced by the site into data/cards.json for Hugo.

Cards are collected from the `commanders` front matter of posts, deck.yaml files
(decklist page bundles) and {{< card "Name" >}} shortcodes in Markdown. Card details come from a local
Scryfall bulk-data file when --bulk is given, otherwise from the Scryfall API.

Each card also gets its roles (data/roles.yaml), pre-filled from Scryfall searches
that are cached in .cache/ for a week. Curators override roles per deck in roles.yaml.
"""

import argparse
import json
import re
import sys
import time
import tomllib
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

import yaml

API_COLLECTION = 'https://api.scryfall.com/cards/collection'
API_SEARCH = 'https://api.scryfall.com/cards/search'
ROLES_FILE = Path('data/roles.yaml')
ROLE_CACHE = Path('.cache/scryfall-roles.json')
ROLE_CACHE_MAX_AGE = timedelta(days=7)
USER_AGENT = 'mcapra.github.io-card-db/1.0'

# Must match the line format parsed by layouts/partials/mtg/parse-line.html
LINE_RE = re.compile(r'^(?:(\d+)x?\s+)?(.+?)(?:\s+\(([A-Za-z0-9]+)\)(?:\s+(\S+))?)?(?:\s+\*[A-Z]\*)*$')
SHORTCODE_RE = re.compile(r'{{<\s*card\s+(?:name=)?(?:"([^"]+)"|`([^`]+)`)')
FRONT_MATTER_RE = re.compile(r'^\+\+\+\n(.*?)\n\+\+\+', re.S)

# Primary type used to group cards, checked in order against the front face
TYPE_ORDER = ['Creature', 'Land', 'Planeswalker', 'Battle', 'Instant', 'Sorcery', 'Artifact', 'Enchantment']


def card_key(name: str, set_code: str = '', number: str = '') -> str:
    """Lookup key shared with the Hugo templates."""
    key = name.strip().lower()
    if set_code and number:
        key += f'|{set_code.lower()}|{number.lower()}'
    return key


def parse_line(line: str) -> dict | None:
    """Parse a Moxfield-style line such as '1 Sol Ring (CMM) 410'."""
    line = line.strip()
    if not line or line.startswith(('#', '//')):
        return None
    m = LINE_RE.match(line)
    if not m:
        return None
    return {'name': m.group(2), 'set': m.group(3) or '', 'number': m.group(4) or ''}


def parse_entry(entry) -> list[dict]:
    """Expand one cards: value (block string, list of strings, or map) into card refs."""
    if isinstance(entry, str):
        return [ref for line in entry.splitlines() if (ref := parse_line(line))]
    if isinstance(entry, list):
        return [ref for item in entry for ref in parse_entry(item)]
    if isinstance(entry, dict) and entry.get('name'):
        return [{'name': entry['name'], 'set': str(entry.get('set', '')), 'number': str(entry.get('number', ''))}]
    return []


def collect_refs(content_dir: Path) -> dict[str, dict]:
    """Find every card referenced under content_dir, keyed by card_key."""
    refs: list[dict] = []
    for deck_path in sorted(content_dir.rglob('deck.yaml')):
        deck = yaml.safe_load(deck_path.read_text(encoding='utf-8')) or {}
        for field in ('cards', 'sideboard'):
            refs += parse_entry(deck.get(field))
        for section in deck.get('sections') or []:
            refs += parse_entry(section.get('cards'))
    for md_path in sorted(content_dir.rglob('*.md')):
        text = md_path.read_text(encoding='utf-8')
        front = FRONT_MATTER_RE.match(text)
        if front:
            refs += parse_entry(tomllib.loads(front.group(1)).get('commanders'))
        refs += [{'name': a or b, 'set': '', 'number': ''} for a, b in SHORTCODE_RE.findall(text)]

    unique = {}
    for ref in refs:
        unique.setdefault(card_key(ref['name'], ref['set'], ref['number']), ref)
    return unique


def primary_type(type_line: str) -> str:
    front = type_line.split('//')[0]
    return next((t for t in TYPE_ORDER if t in front), 'Other')


def summarize(card: dict) -> dict:
    """Reduce a Scryfall card object to the fields the templates use."""
    faces = card.get('card_faces') or []
    front = faces[0] if faces else card
    images = card.get('image_uris') or front.get('image_uris') or {}
    record = {
        'name': card['name'],
        'mana': front.get('mana_cost') or card.get('mana_cost', ''),
        'cmc': card.get('cmc', 0),
        'type': primary_type(card.get('type_line', '')),
        'type_line': card.get('type_line', ''),
        'ci': ''.join(card.get('color_identity', [])),
        'img': images.get('normal', ''),
        'art': images.get('art_crop', ''),
        'uri': card.get('scryfall_uri', '').split('?')[0],
    }
    # Double-faced cards keep separate images per face
    if len(faces) > 1 and 'image_uris' not in card:
        record['back'] = faces[1].get('image_uris', {}).get('normal', '')
    return record


def resolve_bulk(refs: dict[str, dict], bulk_path: Path) -> tuple[dict[str, dict], list[str]]:
    """Resolve refs from a Scryfall bulk file (oracle-cards or default-cards)."""
    print(f'Loading {bulk_path} ...')
    cards = json.loads(bulk_path.read_text(encoding='utf-8'))
    by_name: dict[str, dict] = {}
    by_print: dict[tuple[str, str], dict] = {}
    for card in cards:
        if card.get('layout') in ('art_series', 'token', 'double_faced_token', 'emblem'):
            continue
        by_print[(card['set'], card['collector_number'])] = card
        names = [card['name']] + [f['name'] for f in card.get('card_faces') or []]
        for name in names:
            existing = by_name.get(name.lower())
            # Prefer paper printings with images over digital-only ones
            if existing is None or (existing.get('digital') and not card.get('digital')):
                by_name[name.lower()] = card

    resolved, missing = {}, []
    for key, ref in refs.items():
        card = None
        if ref['set'] and ref['number']:
            card = by_print.get((ref['set'].lower(), ref['number'].lower()))
        card = card or by_name.get(ref['name'].lower())
        if card:
            resolved[key] = summarize(card)
        else:
            missing.append(key)
    return resolved, missing


def scryfall_json(url: str, payload: dict | None = None) -> dict:
    """GET, or POST when a payload is given, with retries and Scryfall's rate-limit backoff."""
    headers = {'User-Agent': USER_AGENT, 'Accept': 'application/json'}
    if payload is not None:
        headers['Content-Type'] = 'application/json'
    data = json.dumps(payload).encode() if payload is not None else None
    request = urllib.request.Request(url, data=data, headers=headers)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.load(response)
        except (TimeoutError, urllib.error.URLError) as e:
            rate_limited = isinstance(e, urllib.error.HTTPError) and e.code == 429
            if (isinstance(e, urllib.error.HTTPError) and not rate_limited) or attempt == 2:
                raise
            # Scryfall asks clients to wait 60 seconds after a 429
            wait = 60 if rate_limited else 2
            print(f'  {e}; retrying in {wait}s ...')
            time.sleep(wait)


def resolve_api(refs: dict[str, dict]) -> tuple[dict[str, dict], list[str]]:
    """Resolve refs through the Scryfall /cards/collection endpoint (75 per request)."""
    items = list(refs.items())
    resolved, missing = {}, []
    for start in range(0, len(items), 75):
        batch = items[start:start + 75]
        identifiers = [
            {'set': ref['set'], 'collector_number': ref['number']} if ref['set'] and ref['number']
            # The collection endpoint rejects full 'Front // Back' names
            else {'name': ref['name'].split(' // ')[0]}
            for _, ref in batch
        ]
        print(f'Fetching {start + 1}-{start + len(batch)} of {len(items)} from Scryfall ...')
        try:
            result = scryfall_json(API_COLLECTION, {'identifiers': identifiers})
        except urllib.error.HTTPError as e:
            print(f'Error: Scryfall returned {e.code}: {e.read().decode()[:200]}', file=sys.stderr)
            sys.exit(1)

        found = result.get('data', [])
        by_print = {(c['set'], c['collector_number']): c for c in found}
        by_name = {}
        for card in found:
            for name in [card['name']] + [f['name'] for f in card.get('card_faces') or []]:
                by_name[name.lower()] = card
        for key, ref in batch:
            card = None
            if ref['set'] and ref['number']:
                card = by_print.get((ref['set'].lower(), ref['number'].lower()))
            card = card or by_name.get(ref['name'].lower())
            if card:
                resolved[key] = summarize(card)
            else:
                missing.append(key)
        time.sleep(0.5)  # /cards/collection is limited to 2 requests per second
    return resolved, missing


def fetch_role_names(roles: list[dict], refresh: bool) -> dict[str, set[str]]:
    """Map each role id to the lowercased card names its Scryfall query matches."""
    queries = {r['id']: r['query'] for r in roles if r.get('query')}
    if not refresh and ROLE_CACHE.exists():
        cache = json.loads(ROLE_CACHE.read_text(encoding='utf-8'))
        fresh = datetime.now(timezone.utc) - datetime.fromisoformat(cache['fetched']) < ROLE_CACHE_MAX_AGE
        if fresh and cache['queries'] == queries:
            return {role: set(names) for role, names in cache['roles'].items()}

    print('Fetching card roles from Scryfall (about two minutes) ...')
    result = {}
    for role, query in queries.items():
        names = set()
        url = f'{API_SEARCH}?{urllib.parse.urlencode({"q": query})}'
        while url:
            try:
                page = scryfall_json(url)
            except urllib.error.HTTPError as e:
                if e.code != 404:  # 404 means the query matched nothing
                    raise
                break
            names.update(card['name'].lower() for card in page['data'])
            url = page.get('next_page') if page.get('has_more') else None
            time.sleep(0.5)  # search shares the 2 requests per second limit
        result[role] = names
        print(f'  {role}: {len(names)} cards')

    ROLE_CACHE.parent.mkdir(parents=True, exist_ok=True)
    ROLE_CACHE.write_text(json.dumps({
        'fetched': datetime.now(timezone.utc).isoformat(),
        'queries': queries,
        'roles': {role: sorted(names) for role, names in result.items()},
    }), encoding='utf-8')
    return result


def main():
    parser = argparse.ArgumentParser(
        description='Build data/cards.json from the cards referenced in site content.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  python build_card_db.py
  python build_card_db.py --bulk ~/Downloads/oracle-cards-20261031.json
  python build_card_db.py --refresh
  python build_card_db.py --refresh-roles
""",
    )
    parser.add_argument('--content', type=Path, default=Path('content'), help='Hugo content directory')
    parser.add_argument('--output', type=Path, default=Path('data/cards.json'), help='Card database to write')
    parser.add_argument('--bulk', type=Path, help='Scryfall bulk-data JSON (oracle-cards or default-cards); uses the API if omitted')
    parser.add_argument('--refresh', action='store_true', help='Re-resolve cards already in the database')
    parser.add_argument('--refresh-roles', action='store_true', help='Re-run the role searches instead of using the weekly cache')
    args = parser.parse_args()

    refs = collect_refs(args.content)
    db = {} if args.refresh or not args.output.exists() else json.loads(args.output.read_text(encoding='utf-8'))
    pending = {k: v for k, v in refs.items() if k not in db}
    print(f'{len(refs)} cards referenced, {len(pending)} to resolve')

    missing = []
    if pending:
        resolve = (lambda r: resolve_bulk(r, args.bulk)) if args.bulk else resolve_api
        resolved, missing = resolve(pending)
        # Printings Scryfall doesn't know fall back to the card's default printing
        retry = {k: dict(pending[k], set='', number='') for k in missing if pending[k]['set']}
        if retry:
            print(f'{len(retry)} printings not found, using default art for: ' + ', '.join(sorted(retry)))
            fallback, _ = resolve(retry)
            resolved.update(fallback)
            missing = [k for k in missing if k not in fallback]
        db.update(resolved)

    # Drop cards no longer referenced so the file stays small
    db = {k: db[k] for k in sorted(db) if k in refs}

    roles = yaml.safe_load(ROLES_FILE.read_text(encoding='utf-8'))
    role_names = fetch_role_names(roles, args.refresh_roles)
    for record in db.values():
        name = record['name'].lower()
        record['roles'] = [r['id'] for r in roles if name in role_names.get(r['id'], ())]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(db, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'Written: {args.output} ({len(db)} cards)')

    if missing:
        print('Not found (check spelling):', file=sys.stderr)
        for key in missing:
            print(f'  {key}', file=sys.stderr)
        sys.exit(2)


if __name__ == '__main__':
    main()
