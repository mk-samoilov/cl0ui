import curses

from ._ctx import ctx, get_color_pair
from cl0ui.stylesheets.text import BaseTextStyle
from cl0ui.markup import parse

_default = BaseTextStyle()


def text(*, text: str, style: BaseTextStyle = None):
    s = style or _default

    screen_row = ctx.row - ctx.scroll_offset + 1
    if ctx.win and 1 <= screen_row < ctx.win_height + 1:
        segments = parse(text, base_attr=s.attr, base_fg=s.fg, base_bg=s.bg)
        col = 2
        for chunk, fg, bg, attr in segments:
            final_attr = attr
            if fg != -1 or bg != -1:
                final_attr |= get_color_pair(fg, bg)
            try:
                ctx.win.addstr(screen_row, col, chunk, final_attr)
            except curses.error:
                pass
            col += len(chunk)

    ctx.row += 1
