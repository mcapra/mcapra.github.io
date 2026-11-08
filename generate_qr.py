#!/usr/bin/env python3
"""Generate a printable QR code (qr.png) linking to each deck's page.

The QR pattern is at least 2cm wide at 300dpi, with the standard white quiet zone
around it, and the file records 300dpi so it prints at true size. Every deck uses the
same QR version, so all codes print the same size. A short label under the code (e.g.
b3tomb) identifies the deck without scanning. The URL and label are stored in the PNG too,
which lets check_decks.py catch a code left stale by renaming a deck.
"""

import argparse
import io
import math
import sys
import tomllib
from pathlib import Path

import segno
from PIL import Image, ImageDraw, ImageFont, PngImagePlugin

from build_card_db import FRONT_MATTER_RE
from check_decks import QR_DPI, QR_FILE, QR_LABEL_KEY, QR_MIN_PIXELS, QR_URL_KEY, page_url, short_label

QR_VERSION = 5   # 37x37 modules: room for URLs up to 84 characters at medium error correction
QUIET_ZONE = 4   # modules of white border; scanners need this, and it's the QR standard's minimum
LABEL_BAND = 44  # pixels of white added under the quiet zone for the label
LABEL_FONT_SIZE = 36  # about 8.5pt at 300dpi


def qr_png(url: str, label: str) -> tuple[bytes, int, int]:
    """Return the PNG bytes, the QR pattern's width and the whole image's width, in pixels."""
    qr = segno.make(url, error='m', version=QR_VERSION, micro=False)
    modules = qr.symbol_size(scale=1, border=0)[0]
    scale = math.ceil(QR_MIN_PIXELS / modules)
    buffer = io.BytesIO()
    qr.save(buffer, kind='png', scale=scale, border=QUIET_ZONE)
    code = Image.open(buffer).convert('L')

    # The label sits in its own band under the quiet zone, so scanning isn't affected
    image = Image.new('L', (code.width, code.height + LABEL_BAND), 255)
    image.paste(code, (0, 0))
    ImageDraw.Draw(image).text((code.width / 2, code.height + LABEL_BAND / 2), label,
                               fill=0, anchor='mm', font=ImageFont.load_default(size=LABEL_FONT_SIZE))
    info = PngImagePlugin.PngInfo()
    info.add_text(QR_URL_KEY, url)
    info.add_text(QR_LABEL_KEY, label)
    output = io.BytesIO()
    image.save(output, format='PNG', dpi=(QR_DPI, QR_DPI), pnginfo=info, optimize=True)
    return output.getvalue(), modules * scale, code.width


def main():
    parser = argparse.ArgumentParser(
        description='Generate a printable QR code for each deck page.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  python generate_qr.py                 # every deck
  python generate_qr.py b3-hashaton     # just these decks
""",
    )
    parser.add_argument('slugs', nargs='*', help='Only these decks (folder names)')
    parser.add_argument('--content', type=Path, default=Path('content/posts/mtg_decklists'), help='Deck posts directory')
    args = parser.parse_args()

    bundles = sorted(p.parent for p in args.content.glob('*/index.md'))
    if args.slugs:
        bundles = [b for b in bundles if b.name in args.slugs]
        missing = set(args.slugs) - {b.name for b in bundles}
        if missing:
            sys.exit(f"No such deck: {', '.join(sorted(missing))}")

    for bundle in bundles:
        front = tomllib.loads(FRONT_MATTER_RE.match((bundle / 'index.md').read_text(encoding='utf-8')).group(1))
        png, pattern, total = qr_png(page_url(bundle.name), short_label(bundle.name, front['commanders'][0]))
        (bundle / QR_FILE).write_bytes(png)
    cm = lambda pixels: pixels / QR_DPI * 2.54
    print(f'{len(bundles)} QR codes written: pattern {pattern}px ({cm(pattern):.2f}cm), '
          f'with quiet zone {total}px ({cm(total):.2f}cm) at {QR_DPI}dpi')


if __name__ == '__main__':
    main()
