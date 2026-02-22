import curses

from ._ctx import ctx, get_color_pair
from cl0ui.stylesheets.button import BaseButtonStyle

_default = BaseButtonStyle()


def button(*, text: str, style: BaseButtonStyle = None) -> bool:
    s = style or _default

    idx = ctx.button_count
    ctx.button_count += 1
    ctx.button_rows.append((ctx.row, 3))

    is_focused = (idx == ctx.focused_idx)
    was_pressed = (idx == ctx.pressed_idx)

    if was_pressed:
        ctx.pressed_idx = None

    if ctx.win:
        attr = s.focused_attr if is_focused else s.attr
        if s.focused_fg != -1 and is_focused:
            attr |= get_color_pair(s.focused_fg, s.focused_bg)
        elif s.fg != -1:
            attr |= get_color_pair(s.fg, s.bg)

        pad = ' ' * s.padding
        inner = s.padding * 2 + len(text)
        top = '\u250c' + '\u2500' * inner + '\u2510'
        mid = '\u2502' + pad + text + pad + '\u2502'
        bot = '\u2514' + '\u2500' * inner + '\u2518'

        for offset, line in ((0, top), (1, mid), (2, bot)):
            screen_row = ctx.row + offset - ctx.scroll_offset + 1
            if not (1 <= screen_row < ctx.win_height + 1):
                continue
            try:
                if offset == 1:
                    ctx.win.addstr(screen_row, 2, '\u2502')
                    ctx.win.addstr(screen_row, 3, pad + text + pad, attr)
                    ctx.win.addstr(screen_row, 3 + len(pad + text + pad), '\u2502')
                else:
                    ctx.win.addstr(screen_row, 2, line)
            except curses.error:
                pass

    ctx.row += 3
    return was_pressed
