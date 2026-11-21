#!/usr/bin/env python3
"""Draw the 20 November 2026 news-image entry: a one-page newspaper front.

Reads nothing, writes entry.png (1024x1024) next to this script.
Run:  python3 generate_image.py
"""

from PIL import Image, ImageDraw, ImageFont

PAGE = 1024
MARGIN = 36
NAVY = (27, 42, 74)
RED = (176, 42, 48)
INK = (28, 28, 28)
GREY = (110, 110, 110)
PAPER = (252, 250, 244)
CARD_LINE = (200, 196, 186)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
SERIF_BOLD = FONT_DIR + "DejaVuSerif-Bold.ttf"
SERIF = FONT_DIR + "DejaVuSerif.ttf"
SANS_BOLD = FONT_DIR + "DejaVuSans-Bold.ttf"
SANS = FONT_DIR + "DejaVuSans.ttf"
SANS_ITALIC = "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"

# (kicker, headline, body, icon)
STORIES = [
    ("UKRAINE",
     "Missiles hit three Kyiv bridges",
     "Three killed and 15 hurt in overnight strikes on the Dnipro crossings, the mayor says.",
     "bridge"),
    ("POLAND",
     "Russian missiles cross into Poland",
     "NATO jets scramble as missiles and a drone fall on Polish soil; Tusk calls it a provocation.",
     "jet"),
    ("SUMMIT",
     "EU and UK strike post-Brexit deal",
     "Food trade, carbon markets and a youth scheme for 100,000 agreed at a rare Brussels summit.",
     "flags"),
    ("MARKETS",
     "Bitcoin sinks below $60,000",
     "First time since July as AI stocks slide; the S&P 500 nears correction territory.",
     "chart"),
    ("CYCLONE",
     "Cyclone Akvan hits India's coast",
     "Third storm in under a month brings heavy rain to the eastern seaboard.",
     "spiral"),
    ("ESTONIA",
     "Estonia to shut its Russia border",
     "Road crossings close from 1 December for at least six months after an alleged sabotage plot.",
     "fence"),
]


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns a list of lines that fit in width pixels."""
    lines, current = [], ""
    for word in text.split():
        trial = word if not current else current + " " + word
        if draw.textlength(trial, font=fnt) <= width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_bridge(d, x, y, s, colour):
    d.line([(x, y + s), (x + s, y + s)], fill=colour, width=4)
    d.arc([x, y, x + s, y + s], start=180, end=360, fill=colour, width=4)
    for frac in (0.2, 0.5, 0.8):
        bx = x + int(s * frac)
        d.line([(bx, y + int(s * 0.55)), (bx, y + s)], fill=colour, width=3)


def draw_jet(d, x, y, s, colour):
    d.polygon([(x + s, y + s // 2), (x, y), (x + s // 3, y + s // 2),
               (x, y + s)], fill=colour)
    d.line([(x + s // 4, y + s // 2), (x + s // 4, y + s)], fill=colour, width=3)


def draw_flags(d, x, y, s, colour):
    d.line([(x + s // 4, y), (x + s // 4, y + s)], fill=colour, width=3)
    d.line([(x + 3 * s // 4, y), (x + 3 * s // 4, y + s)], fill=colour, width=3)
    d.polygon([(x + s // 4, y), (x + s // 2, y + s // 6),
               (x + s // 4, y + s // 3)], fill=colour)
    d.polygon([(x + 3 * s // 4, y), (x + s, y + s // 6),
               (x + 3 * s // 4, y + s // 3)], fill=colour)


def draw_chart(d, x, y, s, colour):
    bars = [0.35, 0.6, 0.45, 0.85]
    bw = s // 5
    for i, h in enumerate(bars):
        bx = x + i * (bw + 3)
        by = y + s - int(s * h)
        d.rectangle([bx, by, bx + bw, y + s], fill=colour)
    d.line([(x, y + int(s * 0.7)), (x + s // 2, y + int(s * 0.45)),
            (x + s, y + int(s * 0.2))], fill=RED, width=4)


def draw_spiral(d, x, y, s, colour):
    for i, r in enumerate((s // 2, s // 3, s // 6)):
        inset = (s // 2 - r)
        d.arc([x + inset, y + inset, x + s - inset, y + s - inset],
              start=200 * i, end=200 * i + 240, fill=colour, width=4)


def draw_fence(d, x, y, s, colour):
    for i in range(5):
        bx = x + i * (s // 4)
        d.line([(bx, y), (bx, y + s)], fill=colour, width=4)
    d.line([(x, y + s // 3), (x + s, y + s // 3)], fill=colour, width=3)
    d.line([(x, y + 2 * s // 3), (x + s, y + 2 * s // 3)], fill=colour, width=3)


ICONS = {"bridge": draw_bridge, "jet": draw_jet, "flags": draw_flags,
         "chart": draw_chart, "spiral": draw_spiral, "fence": draw_fence}


def draw_card(d, box, story):
    kicker, headline, body, icon = story
    x0, y0, x1, y1 = box
    d.line([(x0, y0), (x1, y0)], fill=CARD_LINE, width=2)
    pad = 16
    inner_w = x1 - x0 - 2 * pad
    icon_s = 54
    ICONS[icon](d, x0 + pad, y0 + 14, icon_s, NAVY)
    kx = x0 + pad + icon_s + 14
    kf = font(SANS_BOLD, 20)
    d.text((kx, y0 + 18), kicker, font=kf, fill=RED)
    hf = font(SANS_BOLD, 29)
    hl = wrap(d, headline, hf, inner_w)
    assert len(hl) <= 2, f"headline too long: {headline!r} -> {hl}"
    hy = y0 + 14 + icon_s + 12
    for line in hl:
        d.text((x0 + pad, hy), line, font=hf, fill=INK)
        hy += 36
    bf = font(SANS, 21)
    bl = wrap(d, body, bf, inner_w)
    assert len(bl) <= 3, f"body too long: {body!r} -> {bl}"
    by = hy + 4
    for line in bl:
        d.text((x0 + pad, by), line, font=bf, fill=INK)
        by += 25


def main():
    img = Image.new("RGB", (PAGE, PAGE), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([8, 8, PAGE - 9, PAGE - 9], outline=INK, width=3)

    # Masthead
    title_f = font(SERIF_BOLD, 62)
    title = "THE WORLD IN ONE DAY"
    tw = d.textlength(title, font=title_f)
    d.text(((PAGE - tw) / 2, 30), title, font=title_f, fill=NAVY)
    d.line([(MARGIN, 118), (PAGE - MARGIN, 118)], fill=INK, width=3)
    d.line([(MARGIN, 124), (PAGE - MARGIN, 124)], fill=INK, width=1)

    # Date band
    band_y, band_h = 140, 46
    d.rectangle([MARGIN, band_y, PAGE - MARGIN, band_y + band_h], fill=NAVY)
    date_f = font(SANS_BOLD, 26)
    date = "FRIDAY  \u2022  20 NOVEMBER 2026"
    dw = d.textlength(date, font=date_f)
    d.text(((PAGE - dw) / 2, band_y + 8), date, font=date_f, fill=(255, 255, 255))

    # Subhead
    sub_f = font(SERIF, 24)
    sub = "Six stories that defined the day, from Kyiv to the Indian coast."
    sw = d.textlength(sub, font=sub_f)
    d.text(((PAGE - sw) / 2, 202), sub, font=sub_f, fill=GREY)

    # 2x3 grid of story cards
    grid_top, grid_bottom = 252, 938
    gap = 20
    col_w = (PAGE - 2 * MARGIN - gap) // 2
    row_h = (grid_bottom - grid_top - 2 * gap) // 3
    for i, story in enumerate(STORIES):
        col, row = i % 2, i // 2
        x0 = MARGIN + col * (col_w + gap)
        y0 = grid_top + row * (row_h + gap)
        draw_card(d, (x0, y0, x0 + col_w, y0 + row_h), story)

    # Footer
    d.line([(MARGIN, 962), (PAGE - MARGIN, 962)], fill=INK, width=2)
    foot_f = font(SANS_ITALIC, 19)
    foot = "All six stories above happened or were first reported on 20 November 2026."
    fw = d.textlength(foot, font=foot_f)
    d.text(((PAGE - fw) / 2, 974), foot, font=foot_f, fill=GREY)

    img.save("entry.png")
    print("wrote entry.png")


if __name__ == "__main__":
    main()
