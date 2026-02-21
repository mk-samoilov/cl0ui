import curses

from ._ctx import ctx


def button(*, text: str) -> bool:
    idx = ctx.button_count
    ctx.button_count += 1

    is_focused = (idx == ctx.focused_idx)
    was_pressed = (idx == ctx.pressed_idx)

    if was_pressed:
        ctx.pressed_idx = None

    if ctx.win:
        label = f'[ {text} ]'
        try:
            if is_focused:
                ctx.win.attron(curses.A_REVERSE)
                ctx.win.addstr(ctx.row, 2, label)
                ctx.win.attroff(curses.A_REVERSE)
            else:
                ctx.win.addstr(ctx.row, 2, label)
        except curses.error:
            pass

    ctx.row += 1
    return was_pressed
