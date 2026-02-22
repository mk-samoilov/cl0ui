import re
import curses

from typing import List, Tuple


_TAG_RE = re.compile(r"\[#(\w+)]")

_COLORS = {
    # standard
    "BLACK":          curses.COLOR_BLACK,
    "RED":            curses.COLOR_RED,
    "GREEN":          curses.COLOR_GREEN,
    "YELLOW":         curses.COLOR_YELLOW,
    "BLUE":           curses.COLOR_BLUE,
    "MAGENTA":        curses.COLOR_MAGENTA,
    "CYAN":           curses.COLOR_CYAN,
    "WHITE":          curses.COLOR_WHITE,
    # bright (256-color, 8-15)
    "GRAY":           8,
    "GREY":           8,
    "BRIGHT_RED":     9,
    "BRIGHT_GREEN":   10,
    "LIME":           10,
    "BRIGHT_YELLOW":  11,
    "BRIGHT_BLUE":    12,
    "PINK":           13,
    "BRIGHT_CYAN":    14,
    "BRIGHT_WHITE":   15,
    # extended (256-color)
    "ORANGE":         208,
    "LIGHT_ORANGE":   214,
    "GOLD":           220,
    "PURPLE":         93,
    "VIOLET":         129,
    "NAVY":           18,
    "TEAL":           30,
    "DARK_GREEN":     22,
    "MAROON":         52,
    "DARK_RED":       52,
    "BROWN":          130,
    "SALMON":         210,
    "CORAL":          203,
    "SKY_BLUE":       117,
    "LIGHT_BLUE":     153,
    "INDIGO":         54,
    "OLIVE":          58,
    "MINT":           121,
    "LAVENDER":       183,
    "ROSE":           211,
    "DARK_GRAY":      238,
    "LIGHT_GRAY":     250,
}

_ATTRS = {
    "BOLD":      curses.A_BOLD,
    "DIM":       curses.A_DIM,
    "ITALIC":    curses.A_ITALIC,
    "REVERSE":   curses.A_REVERSE,
    "UNDERLINE": curses.A_UNDERLINE,
    "BLINK":     curses.A_BLINK,
}


def parse(
    text: str,
    base_attr: int = curses.A_NORMAL,
    base_fg: int = -1,
    base_bg: int = -1,
) -> List[Tuple[str, int, int, int]]:
    """Return list of (chunk, fg, bg, attr) segments."""

    segments = []
    cur_fg, cur_bg, cur_attr = base_fg, base_bg, base_attr
    pos = 0

    for m in _TAG_RE.finditer(text):
        if m.start() > pos:
            segments.append((text[pos:m.start()], cur_fg, cur_bg, cur_attr))

        tag = m.group(1).upper()

        if tag == "RESET":
            cur_fg, cur_bg, cur_attr = base_fg, base_bg, base_attr
        elif tag in _COLORS:
            cur_fg = _COLORS[tag]
        elif tag in _ATTRS:
            cur_attr |= _ATTRS[tag]

        pos = m.end()

    if pos < len(text):
        segments.append((text[pos:], cur_fg, cur_bg, cur_attr))

    return segments
