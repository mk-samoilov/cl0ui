import curses

from ._ctx import ctx
from cl0ui.stylesheets.separation import BaseSeparationStyle

_default = BaseSeparationStyle()


def separation(length: int, style: BaseSeparationStyle = None):
    s = style or _default

    if ctx.win:
        try:
            ctx.win.addstr(ctx.row, 2, s.char * length, s.attr)
        except curses.error:
            pass
    ctx.row += 1
