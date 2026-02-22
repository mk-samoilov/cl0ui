import curses

from ._ctx import ctx
from cl0ui.stylesheets.button import BaseButtonStyle

_default = BaseButtonStyle()


def button(*, text: str, style: BaseButtonStyle = None) -> bool:
    s = style or _default

    idx = ctx.button_count
    ctx.button_count += 1

    is_focused = (idx == ctx.focused_idx)
    was_pressed = (idx == ctx.pressed_idx)

    if was_pressed:
        ctx.pressed_idx = None

    if ctx.win:
        attr = s.focused_attr if is_focused else s.attr
        pad = ' ' * s.padding
        inner = s.padding * 2 + len(text)
        top = '\u250c' + '\u2500' * inner + '\u2510'
        mid = '\u2502' + pad + text + pad + '\u2502'
        bot = '\u2514' + '\u2500' * inner + '\u2518'
        try:
            ctx.win.addstr(ctx.row,     2, top)
            ctx.win.addstr(ctx.row + 1, 2, '\u2502')
            ctx.win.addstr(ctx.row + 1, 3, pad + text + pad, attr)
            ctx.win.addstr(ctx.row + 1, 3 + len(pad + text + pad), '\u2502')
            ctx.win.addstr(ctx.row + 2, 2, bot)
        except curses.error:
            pass

    ctx.row += 3
    return was_pressed
