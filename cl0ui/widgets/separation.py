import curses

from ._ctx import ctx
from cl0ui.stylesheets.separation import BaseSeparationStyle

_default = BaseSeparationStyle()


def separation(length: int, style: BaseSeparationStyle = None):
    s = style or _default

    screen_row = ctx.row - ctx.scroll_offset + 1
    if ctx.win and 1 <= screen_row < ctx.win_height + 1:
        try:
            ctx.win.addstr(screen_row, 2, s.char * length, s.attr)
        except curses.error:
            pass

    ctx.row += 1
