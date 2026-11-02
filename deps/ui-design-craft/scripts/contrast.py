#!/usr/bin/env python3
"""WCAG contrast checker for UI color pairs.

Computes the WCAG 2.x contrast ratio between a foreground (text/icon) color and a
background color, and reports whether the pair passes the AA/AAA thresholds for
normal and large text.

Usage:
    python contrast.py "#111827" "#f9fafb"
    python contrast.py --list pairs.txt
    python contrast.py "#fff" "#000" --other "#3b82f6" "#ffffff"

pairs.txt format: one pair per line, "#fg #bg", blank lines and lines starting
with '#' that contain a second token... actually '#' starts a color, so comments
must start with '//' or ';'. Example:

    // primary text on page background
    #111827 #f9fafb
    #ffffff #3b82f6

Thresholds (WCAG 2.x):
    AA  normal text   4.5:1   large text >=18.66px bold or >=24px  3.0:1
    AAA normal text   7.0:1   large text                          4.5:1

Exit status is 0 on success, 2 on a parsing/usage error. It does not fail on a
low contrast ratio; read the output.
"""

from __future__ import annotations

import argparse
import sys


def parse_hex(value: str) -> tuple[int, int, int]:
    """Parse #rgb, #rgba, #rrggbb or #rrggbbaa into 8-bit RGB."""
    s = value.strip().lstrip("#")
    if len(s) == 3:
        s = "".join(c * 2 for c in s)
    elif len(s) == 4:
        s = "".join(c * 2 for c in s)[:6]
    if len(s) == 8:
        s = s[:6]  # ignore alpha; contrast is defined on opaque colors
    if len(s) != 6:
        raise ValueError(f"invalid hex color: {value!r}")
    try:
        return int(s[0:2], 16), int(s[2:4], 16), int(s[4:6], 16)
    except ValueError as exc:
        raise ValueError(f"invalid hex color: {value!r}") from exc


def _channel_luminance(c8: int) -> float:
    c = c8 / 255.0
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def relative_luminance(rgb: tuple[int, int, int]) -> float:
    r, g, b = rgb
    return (
        0.2126 * _channel_luminance(r)
        + 0.7152 * _channel_luminance(g)
        + 0.0722 * _channel_luminance(b)
    )


def contrast_ratio(fg: tuple[int, int, int], bg: tuple[int, int, int]) -> float:
    l1, l2 = relative_luminance(fg), relative_luminance(bg)
    lighter, darker = max(l1, l2), min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def _verdict(ratio: float, threshold: float) -> str:
    return "PASS" if ratio >= threshold else "fail"


def report(fg_raw: str, bg_raw: str) -> float:
    fg, bg = parse_hex(fg_raw), parse_hex(bg_raw)
    ratio = contrast_ratio(fg, bg)
    print(f"{fg_raw} on {bg_raw}  ->  {ratio:.2f}:1")
    print(f"  AA  normal (4.5:1): {_verdict(ratio, 4.5)}"
          f"   large (3.0:1): {_verdict(ratio, 3.0)}")
    print(f"  AAA normal (7.0:1): {_verdict(ratio, 7.0)}"
          f"   large (4.5:1): {_verdict(ratio, 4.5)}")
    return ratio


def parse_pairs(path: str) -> list[tuple[str, str]]:
    pairs: list[tuple[str, str]] = []
    with open(path, "r", encoding="utf-8-sig") as handle:
        for lineno, line in enumerate(handle, 1):
            text = line.strip()
            if not text or text.startswith(("//", ";", "# ")) or text == "#":
                continue
            parts = text.split()
            if len(parts) != 2:
                raise ValueError(f"{path}:{lineno}: expected '<fg> <bg>', got {text!r}")
            pairs.append((parts[0], parts[1]))
    return pairs


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="WCAG contrast checker")
    parser.add_argument("colors", nargs="*", metavar="COLOR",
                        help="foreground and background hex colors")
    parser.add_argument("--list", metavar="FILE",
                        help="file with one '<fg> <bg>' pair per line")
    parser.add_argument("--other", nargs=2, action="append", default=None,
                        metavar=("FG", "BG"),
                        help="additional pair (repeatable)")
    args = parser.parse_args(argv)

    pairs: list[tuple[str, str]] = []
    if args.list:
        pairs.extend(parse_pairs(args.list))
    if len(args.colors) == 2:
        pairs.append((args.colors[0], args.colors[1]))
    elif args.colors:
        parser.error("positional colors must be exactly two: FG BG")
    if args.other:
        pairs.extend((fg, bg) for fg, bg in args.other)

    if not pairs:
        parser.error("provide two colors, --list FILE, or --other FG BG")

    try:
        for index, (fg, bg) in enumerate(pairs):
            if index:
                print()
            report(fg, bg)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
