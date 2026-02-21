import curses

from ._ctx import ctx
from .spacing import spacing as _spacing
from .text import text as _text
from .separation import separation as _separation
from .button import button as _button


class Widgets:
    def _attach(self, win):
        ctx.win = win

    def _begin_frame(self, start_row: int = 0):
        ctx.row = start_row
        ctx.button_count = 0

    def _end_frame(self):
        ctx.total_buttons = ctx.button_count

    def _handle_key(self, key: int):
        if ctx.total_buttons == 0:
            return
        if key == curses.KEY_UP:
            ctx.focused_idx = (ctx.focused_idx - 1) % ctx.total_buttons
        elif key == curses.KEY_DOWN:
            ctx.focused_idx = (ctx.focused_idx + 1) % ctx.total_buttons
        elif key in (curses.KEY_ENTER, ord('\n'), ord('\r'), ord(' ')):
            ctx.pressed_idx = ctx.focused_idx
        ctx.focused_idx = max(0, min(ctx.focused_idx, ctx.total_buttons - 1))

    def spacing(self):
        _spacing()

    def text(self, text: str):
        _text(text=text)

    def separation(self, length: int):
        _separation(length)

    def button(self, text: str) -> bool:
        return _button(text=text)


w = Widgets()
