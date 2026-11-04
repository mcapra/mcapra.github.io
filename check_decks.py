#!/usr/bin/env python3
"""Check deck posts for mistakes before committing (also run in CI before each deploy).

Errors fail the run: missing required front matter, Overview TODOs left in a
published deck, archetypes outside
data/archetypes.yaml, cards missing from data/cards.json, Overview combos or
rulings that name cards not in the deck, bad roles.yaml entries, Mulligan For
land counts that don't match the list, and QR codes that are missing, too small,
point to the wrong URL, or have a wrong or duplicate label.

Warnings don't: decks that aren't 100 cards, missing Overview sections, and with
--spellbook, infinite or game-winning combos (found by Commander Spellbook) that
the Overview doesn't list.
"""

import argparse
import json
import re
import struct
import sys
import time
import tomllib
import urllib.error
import urllib.request
from pathlib import Path

import yaml

from build_card_db import FRONT_MATTER_RE, LINE_RE, USER_AGENT, card_key

SPELLBOOK_FIND = 'https://backend.commanderspellbook.com/find-my-combos'
SPELLBOOK_SOURCE_RE = re.compile(r'^https://commanderspellbook\.com/combo/[\w-]+/$')
LAND_CLAIM_RE = re.compile(r'of the (\d+) lands')
OVERVIEW_SECTIONS = ('strengths', 'weaknesses', 'mulligan')
QR_FILE = 'qr.png'
QR_URL_KEY = 'URL'
QR_LABEL_KEY = 'Label'
QR_DPI = 300
QR_MIN_PIXELS = 237  # 2cm at 300dpi
INCH_PER_METER = 39.3701


def page_url(slug: str) -> str:
    """The published URL of a deck, from baseURL in hugo.toml."""
    base = tomllib.loads(Path('hugo.toml').read_text(encoding='utf-8'))['baseURL']
    return f"{base.rstrip('/')}/posts/mtg_decklists/{slug}/"


def short_label(slug: str, commander: str) -> str:
    """A deck's 6-character ID, e.g. b3-tom-bombadil -> b3tomb. Short slugs use the commander's name."""
    letters = re.sub(r'[^a-z0-9]', '', slug[3:])
    if len(letters) < 4:
        letters = re.sub(r'[^a-z0-9]', '', commander.lower())
    return slug[:2] + letters[:4]


def read_qr(path: Path) -> tuple[int, int, dict[str, str]]:
    """A QR PNG's width in pixels, its dpi and the text recorded by generate_qr.py."""
    data = path.read_bytes()
    width = struct.unpack('>I', data[16:20])[0]
    dpi, text, offset = 0, {}, 8
    while offset < len(data):
        length, kind = struct.unpack('>I4s', data[offset:offset + 8])
        body = data[offset + 8:offset + 8 + length]
        if kind == b'pHYs':
            dpi = round(struct.unpack('>I', body[:4])[0] / INCH_PER_METER)
        elif kind == b'tEXt':
            key, value = body.split(b'\0', 1)
            text[key.decode()] = value.decode()
        offset += length + 12
    return width, dpi, text


def front_name(name: str) -> str:
    return name.split(' // ')[0]


def deck_entries(value) -> list[tuple[int, str, str, str]]:
    """Expand a deck.yaml cards value into (quantity, name, set, number) tuples."""
    if isinstance(value, str):
        out = []
        for line in value.splitlines():
            line = line.strip()
            if not line or line.startswith(('#', '//')):
                continue
            m = LINE_RE.match(line)
            out.append((int(m.group(1) or 1), m.group(2), m.group(3) or '', m.group(4) or ''))
        return out
    if isinstance(value, list):
        return [e for item in value for e in deck_entries(item)]
    if isinstance(value, dict) and value.get('name'):
        return [(int(value.get('qty', 1)), value['name'], str(value.get('set', '')), str(value.get('number', '')))]
    return []


class Report:
    def __init__(self):
        self.errors: dict[str, list[str]] = {}
        self.warnings: dict[str, list[str]] = {}

    def error(self, slug: str, message: str):
        self.errors.setdefault(slug, []).append(message)

    def warn(self, slug: str, message: str):
        self.warnings.setdefault(slug, []).append(message)


def check_deck(post: Path, db: dict, archetypes: set[str], role_ids: set[str], report: Report) -> dict | None:
    """Run the offline checks for one deck. Returns what --spellbook needs, if the deck loaded."""
    slug = post.parent.name
    front = FRONT_MATTER_RE.match(post.read_text(encoding='utf-8'))
    if not front:
        report.error(slug, 'index.md has no TOML front matter')
        return None
    try:
        fm = tomllib.loads(front.group(1))
    except tomllib.TOMLDecodeError as e:
        report.error(slug, f'front matter is not valid TOML: {e}')
        return None

    # Drafts aren't published, so unfinished curation is only a warning there
    unfinished = report.warn if fm.get('draft') else report.error
    for field in ('title', 'bracket', 'commanders'):
        if not fm.get(field):
            report.error(slug, f'missing {field}')
    if not fm.get('archetypes'):
        unfinished(slug, 'missing archetypes')
    if fm.get('bracket') and fm['bracket'] not in range(1, 6):
        report.error(slug, f"bracket {fm['bracket']} is not 1-5")
    for name in fm.get('archetypes', []):
        if name not in archetypes:
            report.error(slug, f'archetype {name!r} is not in data/archetypes.yaml')
    if bool(fm.get('deck_authors')) == bool(fm.get('precon')):
        report.error(slug, 'set exactly one of deck_authors (original list author) or precon (product name)')

    # Every card in the deck, resolved through data/cards.json
    deck_path = post.parent / 'deck.yaml'
    if not deck_path.exists():
        report.error(slug, 'no deck.yaml: run import_decks.py')
        return None
    deck = yaml.safe_load(deck_path.read_text(encoding='utf-8')) or {}
    mainboard = deck_entries(deck.get('cards'))
    for section in deck.get('sections') or []:
        mainboard += deck_entries(section.get('cards'))
    sideboard = deck_entries(deck.get('sideboard'))
    commanders = deck_entries(fm.get('commanders', []))

    names: set[str] = set()   # canonical names, front faces and names as written, lowercased
    lands = total = 0
    missing = []
    for qty, name, set_code, number in commanders + mainboard + sideboard:
        names |= {name.lower(), front_name(name).lower()}
        record = db.get(card_key(name, set_code, number)) or db.get(card_key(name))
        if not record:
            missing.append(name)
            continue
        names |= {record['name'].lower(), front_name(record['name']).lower()}
    for qty, name, set_code, number in mainboard:
        record = db.get(card_key(name, set_code, number)) or db.get(card_key(name))
        if record and record['type'] == 'Land':
            lands += qty
    total = sum(qty for qty, *_ in commanders + mainboard)
    if missing:
        report.error(slug, f"{len(missing)} cards not in data/cards.json (run build_card_db.py): {', '.join(missing[:5])}")
    if total != 100:
        report.warn(slug, f'deck has {total} cards (commanders + main deck), not 100')

    in_deck = lambda name: name.lower() in names or front_name(name).lower() in names

    # Overview
    overview = fm.get('overview') or {}
    if not overview.get('summary'):
        unfinished(slug, 'missing [overview] summary')
    if 'TODO' in json.dumps(overview):
        unfinished(slug, 'Overview still has TODO placeholders from ingest_deck.py')
    for section in OVERVIEW_SECTIONS:
        if overview and not overview.get(section):
            report.warn(slug, f'Overview has no {section}')
    for combo in overview.get('combos', []):
        for name in combo.get('cards', []):
            if not in_deck(name):
                report.error(slug, f'Key Combos card {name!r} is not in the deck')
        if not combo.get('result'):
            report.error(slug, f"combo {' + '.join(combo.get('cards', []))} has no result")
        if combo.get('kind') not in (None, 'infinite', 'win'):
            report.error(slug, f"combo kind {combo['kind']!r} must be 'infinite' or 'win'")
        if combo.get('source') and not SPELLBOOK_SOURCE_RE.match(combo['source']):
            report.error(slug, f"combo source {combo['source']!r} is not a Commander Spellbook combo URL")
    for ruling in overview.get('rulings', []):
        for name in ruling.get('cards', []):
            if not in_deck(name):
                report.error(slug, f'Rulings card {name!r} is not in the deck')
    for line in overview.get('mulligan', []):
        for claimed in LAND_CLAIM_RE.findall(line):
            if int(claimed) != lands:
                report.error(slug, f'Mulligan For says {claimed} lands; the deck has {lands}')

    # Printable QR code
    qr_path = post.parent / QR_FILE
    if not qr_path.exists():
        unfinished(slug, f'no {QR_FILE}: run generate_qr.py')
    else:
        width, dpi, text = read_qr(qr_path)
        if text.get(QR_URL_KEY) != page_url(slug):
            report.error(slug, f'{QR_FILE} points to {text.get(QR_URL_KEY, "an unknown URL")}, not {page_url(slug)}: run generate_qr.py')
        if fm.get('commanders') and text.get(QR_LABEL_KEY) != short_label(slug, fm['commanders'][0]):
            report.error(slug, f"{QR_FILE} is labeled {text.get(QR_LABEL_KEY)}, not {short_label(slug, fm['commanders'][0])}: run generate_qr.py")
        if dpi != QR_DPI or width < QR_MIN_PIXELS:
            report.error(slug, f'{QR_FILE} is {width}px at {dpi}dpi, too small to print at 2cm: run generate_qr.py')

    # Curator role overrides
    roles_path = post.parent / 'roles.yaml'
    overrides = (yaml.safe_load(roles_path.read_text(encoding='utf-8')) or {}) if roles_path.exists() else {}
    for name, roles in overrides.items():
        if not in_deck(name):
            report.error(slug, f'roles.yaml lists {name!r}, which is not in the deck')
        for role in roles or []:
            if role not in role_ids:
                report.error(slug, f'roles.yaml gives {name!r} unknown role {role!r} (see data/roles.yaml)')

    return {
        'label': short_label(slug, fm['commanders'][0]) if fm.get('commanders') else slug,
        'commanders': [name for _, name, _, _ in commanders],
        'cards': [name for _, name, _, _ in mainboard],
        'listed': [{n.lower() for n in c.get('cards', [])} | {front_name(n).lower() for n in c.get('cards', [])}
                   for c in overview.get('combos', [])],
    }


def find_decisive_combos(commanders: list[str], cards: list[str]) -> list[dict]:
    """Ask Commander Spellbook for the deck's infinite or game-winning combos."""
    payload = json.dumps({
        'commanders': [{'card': n, 'quantity': 1} for n in commanders],
        'main': [{'card': n, 'quantity': 1} for n in cards],
    }).encode()
    request = urllib.request.Request(SPELLBOOK_FIND, data=payload, headers={
        'User-Agent': USER_AGENT, 'Accept': 'application/json', 'Content-Type': 'application/json'})
    with urllib.request.urlopen(request, timeout=60) as response:
        result = json.load(response)
    combos = (result.get('results') or result).get('included', [])
    return [c for c in combos if any(re.search(r'infinite|win the game', p['feature']['name'], re.I) for p in c['produces'])]


def check_spellbook(slug: str, deck: dict, report: Report):
    """Warn when Commander Spellbook finds infinite or game-winning combos the Overview doesn't list."""
    try:
        decisive = find_decisive_combos(deck['commanders'], deck['cards'])
    except (urllib.error.URLError, TimeoutError) as e:
        report.warn(slug, f'Commander Spellbook check failed: {e}')
        return
    if not decisive:
        return
    # Listed if every piece of some decisive combo appears together in one Overview combo
    for combo in decisive:
        pieces = {front_name(u['card']['name']).lower() for u in combo['uses']}
        if any(pieces <= listed for listed in deck['listed']):
            return
    simplest = min(decisive, key=lambda c: len(c['uses']))
    report.warn(slug, f"{len(decisive)} infinite/winning combos on Commander Spellbook but none in Key Combos, "
                      f"e.g. {' + '.join(u['card']['name'] for u in simplest['uses'])} "
                      f"(https://commanderspellbook.com/combo/{simplest['id']}/)")


def main():
    parser = argparse.ArgumentParser(
        description='Check deck posts for mistakes before committing.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  python check_decks.py                 # every deck, offline
  python check_decks.py b4-hashaton     # just these decks
  python check_decks.py --spellbook     # also look for unlisted infinite combos (online)
""",
    )
    parser.add_argument('slugs', nargs='*', help='Only check these decks (folder names)')
    parser.add_argument('--content', type=Path, default=Path('content/posts/mtg_decklists'), help='Deck posts directory')
    parser.add_argument('--spellbook', action='store_true', help='Ask Commander Spellbook for combos the Overview should list')
    parser.add_argument('--strict', action='store_true', help='Fail on warnings too')
    args = parser.parse_args()

    db = json.loads(Path('data/cards.json').read_text(encoding='utf-8'))
    archetypes = {a['name'] for a in yaml.safe_load(Path('data/archetypes.yaml').read_text(encoding='utf-8'))}
    role_ids = {r['id'] for r in yaml.safe_load(Path('data/roles.yaml').read_text(encoding='utf-8'))}

    report = Report()
    posts = sorted(args.content.glob('*/index.md'))
    if args.slugs:
        posts = [p for p in posts if p.parent.name in args.slugs]
    labels = {}
    for post in posts:
        deck = check_deck(post, db, archetypes, role_ids, report)
        if deck and deck['label'] in labels:
            report.error(post.parent.name, f"QR label {deck['label']} is already used by {labels[deck['label']]}: rename one deck's folder")
        elif deck:
            labels[deck['label']] = post.parent.name
        if deck and args.spellbook:
            check_spellbook(post.parent.name, deck, report)
            time.sleep(1)  # be gentle with Commander Spellbook

    for slug in sorted(set(report.errors) | set(report.warnings)):
        print(slug)
        for message in report.errors.get(slug, []):
            print(f'  error: {message}')
        for message in report.warnings.get(slug, []):
            print(f'  warning: {message}')
    errors = sum(map(len, report.errors.values()))
    warnings = sum(map(len, report.warnings.values()))
    print(f'{len(posts)} decks checked: {errors} errors, {warnings} warnings')
    if errors or (args.strict and warnings):
        sys.exit(1)


if __name__ == '__main__':
    main()
