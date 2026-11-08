#!/usr/bin/env python3
"""Import card lists for deck posts from their `decklist_url` (Moxfield or Archidekt).

Each deck post becomes a page bundle (b4-foo.md -> b4-foo/index.md) with a
generated deck.yaml. The post's `commanders` front matter is updated when the
source lists different commanders (e.g. a partner that was missing).

Generated files start with IMPORT_MARKER; files without it were written by hand
and are never overwritten. Run build_card_db.py afterwards.
"""

import argparse
import json
import re
import sys
import time
import tomllib
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

USER_AGENT = 'mcapra.github.io-deck-import/1.0'
IMPORT_MARKER = '# Imported by import_decks.py'
FRONT_MATTER_RE = re.compile(r'^\+\+\+\n(.*?)\n\+\+\+', re.S)
MOXFIELD_RE = re.compile(r'moxfield\.com/decks/([\w-]+)')
ARCHIDEKT_RE = re.compile(r'archidekt\.com/decks/(\d+)')


def fetch_json(url: str) -> dict:
    request = urllib.request.Request(url, headers={'User-Agent': USER_AGENT, 'Accept': 'application/json'})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


# A card is (quantity, name, set code, collector number); the printing keeps the deck's art
Card = tuple[int, str, str, str]


def board(cards: dict) -> list[Card]:
    return [(c['quantity'], c['card']['name'], c['card']['set'], c['card']['cn']) for c in cards.values()]


def line(card: Card) -> str:
    qty, name, set_code, number = card
    return f'{qty} {name} ({set_code.upper()}) {number}' if set_code and number else f'{qty} {name}'


def from_moxfield(deck_id: str) -> dict:
    data = fetch_json(f'https://api2.moxfield.com/v3/decks/all/{deck_id}')
    boards = data['boards']
    # A duplicated deck credits the builder of the original, not whoever copied it
    original = data.get('originalDeck') or data
    return {
        'name': original.get('name') or data['name'],
        'bracket': data.get('userBracket') or data.get('bracket') or data.get('autoBracket'),
        'updated': data.get('lastUpdatedAtUtc', ''),
        'author': original['createdByUser']['userName'],
        'author_url': f"https://moxfield.com/users/{original['createdByUser']['userName']}",
        'commanders': [line(c).split(' ', 1)[1] for c in board(boards['commanders']['cards'])],
        'cards': board(boards['mainboard']['cards']) + board(boards.get('companions', {}).get('cards', {})),
        'sideboard': board(boards.get('sideboard', {}).get('cards', {})),
    }


def from_archidekt(deck_id: str) -> dict:
    data = fetch_json(f'https://archidekt.com/api/decks/{deck_id}/')
    # Categories such as Maybeboard and Sideboard are excluded from the deck
    outside = {c['name'] for c in data.get('categories', []) if not c.get('includedInDeck', True)}
    result = {
        'name': data['name'],
        'bracket': data.get('edhBracket'),
        'updated': data.get('updatedAt', ''),
        'author': data['owner']['username'],
        'author_url': f"https://archidekt.com/u/{data['owner']['username']}",
        'commanders': [], 'cards': [], 'sideboard': [],
    }
    for entry in data['cards']:
        if entry.get('deletedAt'):
            continue
        card = entry['card']
        printing = (entry['quantity'], card['oracleCard']['name'], card['edition']['editioncode'], card['collectorNumber'])
        categories = entry.get('categories') or []
        if 'Commander' in categories:
            result['commanders'].append(line(printing).split(' ', 1)[1])
        elif 'Sideboard' in categories:
            result['sideboard'].append(printing)
        elif not outside.intersection(categories[:1]):
            result['cards'].append(printing)
    return result


def render_yaml(deck: dict, url: str) -> str:
    def block(cards):
        return ''.join(f'  {line(card)}\n' for card in sorted(cards, key=lambda c: c[1]))
    text = f'{IMPORT_MARKER} from {url} on {date.today().isoformat()}.\n'
    text += '# Re-run `python import_decks.py --refresh` to update, or delete this header to edit by hand.\n\n'
    text += 'cards: |\n' + block(deck['cards'])
    if deck['sideboard']:
        text += '\nsideboard: |\n' + block(deck['sideboard'])
    return text


def toml_list(values: list[str]) -> str:
    return '[' + ', '.join(f'"{v}"' if "'" in v else f"'{v}'" for v in values) + ']'


def find_posts(content: Path) -> list[Path]:
    posts = [p for p in content.glob('*.md') if p.name != '_index.md'] + list(content.glob('*/index.md'))
    return sorted(posts)


def main():
    parser = argparse.ArgumentParser(
        description='Import deck card lists from Moxfield or Archidekt into deck.yaml files.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  python import_decks.py                  # decks without a deck.yaml
  python import_decks.py --refresh        # also re-import previously imported decks
  python import_decks.py b3-hashaton      # just these posts
""",
    )
    parser.add_argument('slugs', nargs='*', help='Only import these posts (file or folder names)')
    parser.add_argument('--content', type=Path, default=Path('content/posts/mtg_decklists'), help='Deck posts directory')
    parser.add_argument('--refresh', action='store_true', help='Re-import decks whose deck.yaml was generated by this script')
    args = parser.parse_args()

    failures = []
    for post in find_posts(args.content):
        slug = post.parent.name if post.name == 'index.md' else post.stem
        if args.slugs and slug not in args.slugs:
            continue
        text = post.read_text(encoding='utf-8')
        front = FRONT_MATTER_RE.match(text)
        params = tomllib.loads(front.group(1)) if front else {}
        url = params.get('decklist_url', '')

        deck_yaml = post.parent / 'deck.yaml' if post.name == 'index.md' else None
        if deck_yaml and deck_yaml.exists():
            if not deck_yaml.read_text(encoding='utf-8').startswith(IMPORT_MARKER):
                print(f'{slug}: skipped, deck.yaml was edited by hand')
                continue
            if not args.refresh:
                continue

        if m := MOXFIELD_RE.search(url):
            source = lambda: from_moxfield(m.group(1))
        elif m := ARCHIDEKT_RE.search(url):
            source = lambda: from_archidekt(m.group(1))
        else:
            print(f'{slug}: skipped, unsupported decklist_url {url!r}')
            continue

        try:
            deck = source()
        except (urllib.error.URLError, TimeoutError, KeyError) as e:
            print(f'{slug}: FAILED ({e})', file=sys.stderr)
            failures.append(slug)
            continue
        finally:
            time.sleep(1)  # be gentle with the deck sites

        # Single-file post -> page bundle so deck.yaml can sit next to it
        if post.name != 'index.md':
            bundle = post.with_suffix('')
            bundle.mkdir()
            post = post.rename(bundle / 'index.md')
            deck_yaml = bundle / 'deck.yaml'

        deck_yaml.write_text(render_yaml(deck, url), encoding='utf-8')
        count = sum(card[0] for card in deck['cards']) + len(deck['commanders'])
        note = ''
        if deck['commanders'] and deck['commanders'] != params.get('commanders'):
            text = re.sub(r'^commanders = .*$', lambda _: f"commanders = {toml_list(deck['commanders'])}", text, count=1, flags=re.M)
            post.write_text(text, encoding='utf-8')
            note = f", commanders now {deck['commanders']}"
        print(f'{slug}: {count} cards{note}')

    if failures:
        print(f'{len(failures)} failed: {" ".join(failures)}', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
