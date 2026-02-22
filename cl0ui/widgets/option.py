import curses

from ._ctx import ctx, get_color_pair
from cl0ui.stylesheets.option import BaseOptionStyle

_default = BaseOptionStyle()


def option(*, text: str, style: BaseOptionStyle = None) -> bool:
    s = style or _default

    idx = ctx.button_count
    ctx.button_count += 1

    is_focused = (idx == ctx.focused_idx)
    was_pressed = (idx == ctx.pressed_idx)

    if was_pressed:
        ctx.pressed_idx = None

    if ctx.win:
        if is_focused:
            attr = s.focused_attr
            fg, bg = s.focused_fg, s.focused_bg
        else:
            attr = s.attr
            fg, bg = s.fg, s.bg

        if fg != -1 or bg != -1:
            attr |= get_color_pair(fg, bg)

        try:
            ctx.win.addstr(ctx.row, 2, f'[ {text} ]', attr)
        except curses.error:
            pass

    ctx.row += 1
    return was_pressed
