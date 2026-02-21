import curses

from ._ctx import ctx


def text(*, text: str):
    if ctx.win:
        try:
            ctx.win.addstr(ctx.row, 2, text)
        except curses.error:
            pass
    ctx.row += 1
