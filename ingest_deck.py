#!/usr/bin/env python3
"""Turn a Moxfield or Archidekt deck URL into a draft deck post, in one command.

Creates the page bundle (index.md, deck.yaml, roles.yaml, qr.png) with bracket, commanders
and author filled in, resolves the cards, and adds Commander Spellbook's infinite combos to
Key Combos. The Overview prose needs judgment, so it's left as TODO placeholders, and a
research brief with the facts for writing it goes to .cache/ingest/<slug>.md.

Moxfield has no public primer endpoint. To include a primer, save its JSON from the
browser and pass it with --primer. Re-running on an existing deck only rewrites the brief.
"""

import argparse
import collections
import json
import re
import subprocess
import sys
import tomllib
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

import yaml

from build_card_db import API_COLLECTION, LINE_RE, card_key, scryfall_json
from check_decks import find_decisive_combos, front_name
from import_decks import ARCHIDEKT_RE, MOXFIELD_RE, from_archidekt, from_moxfield, render_yaml, toml_list

ROLES_TEMPLATE = Path('archetypes/decklist/roles.yaml')
BRIEF_DIR = Path('.cache/ingest')
MAX_COMBOS = 3
TYPE_ORDER = ['Creature', 'Planeswalker', 'Battle', 'Instant', 'Sorcery', 'Artifact', 'Enchantment', 'Land', 'Other']
s = lambda value: json.dumps(value, ensure_ascii=False)  # JSON strings are valid TOML basic strings


def fetch_deck(url: str) -> dict:
    if m := MOXFIELD_RE.search(url):
        return from_moxfield(m.group(1))
    if m := ARCHIDEKT_RE.search(url):
        return from_archidekt(m.group(1))
    sys.exit(f'Not a Moxfield or Archidekt deck URL: {url}')


def default_slug(bracket: int, commanders: list[str]) -> str:
    """b2-tom-bombadil: the first commander's name, up to any comma, without a leading 'The'."""
    name = re.sub(r'\s+\(\w+\)\s+\S+$', '', commanders[0]).split(',')[0]
    name = re.sub(r'^the\s+', '', name, flags=re.I).lower()
    return f"b{bracket}-{re.sub(r'[^a-z0-9]+', '-', name.replace(chr(39), '')).strip('-')}"


def combo_toml(combo: dict) -> str:
    """A Commander Spellbook combo as an [[overview.combos]] block."""
    produces = [p['feature']['name'] for p in combo['produces']]
    kind = 'infinite' if any('infinite' in p.lower() for p in produces) else 'win'
    result = ', '.join(p[0].lower() + p[1:] for p in produces[:3])
    steps = [line.strip() for line in combo.get('description', '').splitlines() if line.strip()]
    block = ['', '[[overview.combos]]',
             f"cards = [{', '.join(s(u['card']['name']) for u in combo['uses'])}]",
             f'result = {s(result[0].upper() + result[1:] + ".")}',
             f'kind = {s(kind)}']
    if steps:
        block.append('steps = [\n' + ''.join(f'  {s(x)},\n' for x in steps) + ']')
    block.append(f"source = {s(f'https://commanderspellbook.com/combo/{combo['id']}/')}")
    return '\n'.join(block)


def post_text(deck: dict, url: str, combos: list[dict], precon: str | None) -> str:
    credit = f'precon = {s(precon)}' if precon else (
        f"deck_authors = [{{ name = {s(deck['author'])}, url = {s(deck['author_url'])} }}]")
    title = re.sub(r'\s+\(\w+\)\s+\S+$', '', deck['commanders'][0])
    updated = deck['updated'] or datetime.now(timezone.utc).isoformat()
    date = datetime.fromisoformat(updated.replace('Z', '+00:00')).strftime('%Y-%m-%dT%H:%M:%S%z')
    lines = ['+++',
             f"title = {s(f'[Bracket {deck['bracket']}] {title}')}",
             f"bracket = {deck['bracket']}",
             f"commanders = {toml_list(deck['commanders'])}",
             'archetypes = []  # TODO: primary first, from data/archetypes.yaml',
             f'decklist_url = {s(url)}',
             credit,
             f'date = {date[:-2]}:{date[-2:]}',
             'draft = true',
             '',
             '[overview]',
             'summary = "TODO: colors, engine and win route in one or two sentences."',
             'strengths = ["TODO"]',
             'weaknesses = ["TODO"]',
             'gameplan = ["TODO"]',
             'mulligan = ["TODO: lands and the colors that carry the deck", "TODO: what the first turns need"]']
    lines += [combo_toml(c) for c in combos[:MAX_COMBOS]]
    return '\n'.join(lines) + '\n+++\n'


def primer_text(path: Path) -> str:
    """Moxfield primer JSON to readable text: [[Card|set|id]] -> Card, [[symbol:r]] -> {R}."""
    text = json.loads(path.read_text(encoding='utf-8')).get('content', '')
    text = re.sub(r'\[\[symbol:(\w+)\]\]', lambda m: f'{{{m.group(1).upper()}}}', text)
    text = re.sub(r'\[\[([^\]|]+)(?:\|[^\]]*)?\]\]', r'\1', text)
    return re.sub(r'^===\w*(:.*)?$', lambda m: (m.group(1) or '').lstrip(':'), text, flags=re.M)


def brief_text(slug: str, deck: dict, combos: list[dict], primer: str) -> str:
    """The facts for writing the Overview, in the terms README.md's guidance asks for."""
    db = json.loads(Path('data/cards.json').read_text(encoding='utf-8'))
    parsed = [LINE_RE.match(c) for c in deck['commanders']]
    commanders = [db[card_key(m.group(2), m.group(3) or '', m.group(4) or '')] for m in parsed]
    main = yaml.safe_load(Path(f'content/posts/mtg_decklists/{slug}/deck.yaml').read_text(encoding='utf-8'))['cards']
    cards = []
    for line in main.splitlines():
        m = LINE_RE.match(line.strip())
        cards.append((int(m.group(1) or 1), db[card_key(m.group(2), m.group(3) or '', m.group(4) or '')]))

    oracle = scryfall_json(API_COLLECTION, {'identifiers': [{'name': front_name(c['name'])} for c in commanders]})
    pips, roles, cheap, curve = (collections.Counter() for _ in range(4))
    by_type = collections.defaultdict(list)
    for qty, card in cards:
        by_type[card['type']].append(f"{qty} {card['name']} {card['mana']}" + (f" [{', '.join(card['roles'])}]" if card['roles'] else ''))
        pips.update({sym: qty * n for sym, n in collections.Counter(re.findall(r'\{([WUBRG])\}', card['mana'])).items()})
        roles.update({r: qty for r in card['roles']})
        if card['type'] != 'Land':
            curve[min(int(card['cmc']), 7)] += qty
            cheap.update({r: qty for r in card['roles'] if r in ('mana-dork', 'mana-rock', 'land-ramp', 'ritual') and card['cmc'] <= 2})

    out = [f"# Ingest brief: {slug}", '',
           f"Source: {deck['name']} by {deck['author']} (bracket {deck['bracket']})", '', '## Commanders']
    for card in oracle['data']:
        text = card.get('oracle_text') or ' // '.join(f.get('oracle_text', '') for f in card.get('card_faces', []))
        out += [f"- **{card['name']}** {card.get('mana_cost', '')} ({card['type_line']}): {text}"]
    out += ['', '## Numbers (for Mulligan For)',
            f"- Lands: {sum(q for q, c in cards if c['type'] == 'Land')}",
            f'- Colored mana symbols: {dict(pips.most_common())}',
            f'- Cheap ramp (2 mana or less): {dict(cheap)}',
            f'- Curve (nonland, 7 = 7+): {dict(sorted(curve.items()))}',
            f'- Roles: {dict(roles.most_common())}',
            '', '## Commander Spellbook infinite/winning combos']
    out += [f"- {' + '.join(u['card']['name'] for u in c['uses'])}: {', '.join(p['feature']['name'] for p in c['produces'][:3])}" for c in combos] or ['- None found']
    out += ['', '## Cards']
    for card_type in TYPE_ORDER:
        if by_type[card_type]:
            out += [f'### {card_type}'] + [f'- {line}' for line in sorted(by_type[card_type])]
    out += ['', '## Primer', primer or '(none supplied)', '']
    return '\n'.join(out)


def main():
    parser = argparse.ArgumentParser(
        description='Turn a Moxfield or Archidekt deck URL into a draft deck post.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  python ingest_deck.py https://moxfield.com/decks/XXXXXXXX
  python ingest_deck.py URL --bracket 3 --slug b3-my-deck
  python ingest_deck.py URL --primer input/my_primer.json
  python ingest_deck.py URL --precon 'Animated Army'
""",
    )
    parser.add_argument('url', help='Moxfield or Archidekt deck URL')
    parser.add_argument('--bracket', type=int, help='Override the bracket reported by the source')
    parser.add_argument('--slug', help='Post folder name (default: b<bracket>-<commander>)')
    parser.add_argument('--precon', help='Product name for a preconstructed deck, instead of crediting an author')
    parser.add_argument('--primer', type=Path, help='Primer JSON saved from Moxfield, included in the brief')
    args = parser.parse_args()

    deck = fetch_deck(args.url)
    deck['bracket'] = args.bracket or deck['bracket']
    if not deck['bracket']:
        sys.exit('The source reports no bracket; pass --bracket.')
    slug = args.slug or default_slug(deck['bracket'], deck['commanders'])
    bundle = Path('content/posts/mtg_decklists') / slug
    names = [LINE_RE.match(c).group(2) for c in deck['commanders']]

    try:
        combos = find_decisive_combos(names, [card[1] for card in deck['cards']])
    except (urllib.error.URLError, TimeoutError) as e:
        print(f'Warning: Commander Spellbook lookup failed, add combos by hand: {e}', file=sys.stderr)
        combos = []
    combos.sort(key=lambda c: len(c['uses']))

    if bundle.exists():
        print(f'{slug}: already exists, only rewriting the brief')
    else:
        bundle.mkdir(parents=True)
        (bundle / 'deck.yaml').write_text(render_yaml(deck, args.url), encoding='utf-8')
        (bundle / 'roles.yaml').write_text(ROLES_TEMPLATE.read_text(encoding='utf-8'), encoding='utf-8')
        text = post_text(deck, args.url, combos, args.precon)
        tomllib.loads(text.split('+++')[1])
        (bundle / 'index.md').write_text(text, encoding='utf-8')
        print(f"{slug}: created, credited to {args.precon or deck['author']}, {min(len(combos), MAX_COMBOS)} of {len(combos)} Spellbook combos added")
        if subprocess.run([sys.executable, 'build_card_db.py']).returncode:
            sys.exit('build_card_db.py reported problems; fix them and re-run to write the brief.')

    if subprocess.run([sys.executable, 'generate_qr.py', slug]).returncode:
        sys.exit('generate_qr.py failed; fix it and re-run to write the brief.')

    BRIEF_DIR.mkdir(parents=True, exist_ok=True)
    brief = BRIEF_DIR / f'{slug}.md'
    brief.write_text(brief_text(slug, deck, combos, primer_text(args.primer) if args.primer else ''), encoding='utf-8')
    print(f'Next: write the Overview in {bundle}/index.md using {brief}, then run check_decks.py --spellbook {slug}')


if __name__ == '__main__':
    main()
