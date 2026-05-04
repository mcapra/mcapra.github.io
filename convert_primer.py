#!/usr/bin/env python3
"""Convert a Moxfield primer JSON export to Hugo-compatible Markdown."""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


def parse_date(date_str: str) -> str:
    """Convert an ISO UTC timestamp to Hugo TOML date format."""
    # Normalize fractional seconds to microseconds and add UTC offset
    date_str = re.sub(r'\.(\d+)Z$', lambda m: f'.{m.group(1)[:6].ljust(6, "0")}+00:00', date_str)
    date_str = re.sub(r'Z$', '+00:00', date_str)
    try:
        dt = datetime.fromisoformat(date_str)
    except ValueError:
        dt = datetime.now(timezone.utc)
    return dt.isoformat(timespec='seconds')


def toml_string(value: str) -> str:
    """Format a string value for TOML front matter, choosing quote style as needed."""
    if "'" in value:
        escaped = value.replace('\\', '\\\\').replace('"', '\\"')
        return f'"{escaped}"'
    return f"'{value}'"


def convert_youtube(text: str) -> str:
    """Convert [[youtube:VIDEO_ID...]] to a plain YouTube URL."""
    def replace(m):
        video_id = m.group(1).split('?')[0]
        return f'https://www.youtube.com/watch?v={video_id}'
    return re.sub(r'\[\[youtube:([^\]]+)\]\]', replace, text)


def convert_symbols(text: str) -> str:
    """Convert [[symbol:X]] to {X}."""
    return re.sub(r'\[\[symbol:(\w+)\]\]', lambda m: f'{{{m.group(1).upper()}}}', text)


def convert_card_links(text: str) -> str:
    """Convert [[CardName|Set|ID]] and [[CardName]] to plain card name text."""
    text = re.sub(r'\[\[([^\]|]+)\|[^\]]*\]\]', r'\1', text)
    text = re.sub(r'\[\[([^\]]+)\]\]', r'\1', text)
    return text


def convert_moxfield_markup(content: str) -> str:
    """Convert Moxfield panel/accordion markup and inline syntax to Markdown."""
    lines = content.split('\n')
    result = []
    accordion_depth = 0

    for line in lines:
        stripped = line.strip()

        if stripped == '===accordion':
            accordion_depth += 1
            continue

        if stripped == '===endaccordion':
            accordion_depth = max(0, accordion_depth - 1)
            continue

        if stripped.startswith('===panel:'):
            panel_title = stripped[len('===panel:'):].strip()
            level = '#' * (accordion_depth + 1)
            result.append(f'{level} {panel_title}')
            continue

        if stripped in ('===endpanel', '===center', '===endcenter'):
            continue

        result.append(line)

    text = '\n'.join(result)

    # Order matters: youtube and symbols before generic card-link pattern
    text = convert_youtube(text)
    text = convert_symbols(text)
    text = convert_card_links(text)

    # Collapse runs of more than two blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)

    return text.strip()


def convert(json_path: Path, title: str, output_path: Path) -> None:
    data = json.loads(json_path.read_text(encoding='utf-8'))

    content = data.get('content', '')
    last_updated = data.get('lastUpdatedAtUtc', '')
    date = parse_date(last_updated) if last_updated else datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S%z')

    body = convert_moxfield_markup(content)

    front_matter = f"""\
+++
title = {toml_string(title)}
date = {date}
draft = false
+++"""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(f'{front_matter}\n\n{body}\n', encoding='utf-8')
    print(f'Written: {output_path}')


def main():
    parser = argparse.ArgumentParser(
        description='Convert a Moxfield primer JSON to Hugo Markdown.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  python convert_primer.py input/heirgast_primer.json \\
      --title "[Bracket 3] Herigast, Erupting Nullkite" \\
      --output content/posts/mtg_decklists/b3-herigast.md
""",
    )
    parser.add_argument('input', type=Path, help='Moxfield primer JSON file')
    parser.add_argument('--title', required=True, help='Hugo post title')
    parser.add_argument(
        '--output', type=Path,
        help='Output .md path (default: content/posts/mtg_decklists/<stem-without-_primer>.md)',
    )
    args = parser.parse_args()

    if not args.input.exists():
        print(f'Error: {args.input} not found', file=sys.stderr)
        sys.exit(1)

    output = args.output
    if output is None:
        slug = re.sub(r'_primer$', '', args.input.stem)
        output = Path('content/posts/mtg_decklists') / f'{slug}.md'

    convert(args.input, args.title, output)


if __name__ == '__main__':
    main()
