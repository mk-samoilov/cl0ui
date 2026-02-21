import curses

from ._ctx import ctx


def separation(length: int):
    if ctx.win:
        try:
            ctx.win.addstr(ctx.row, 2, '\u2500' * length)
        except curses.error:
            pass
    ctx.row += 1
