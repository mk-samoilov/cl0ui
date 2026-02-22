import curses

from ._ctx import ctx
from .spacing import spacing as _spacing
from .text import text as _text
from .separation import separation as _separation
from .button import button as _button
from .option import option as _option
from cl0ui.stylesheets.button import BaseButtonStyle
from cl0ui.stylesheets.option import BaseOptionStyle
from cl0ui.stylesheets.text import BaseTextStyle
from cl0ui.stylesheets.separation import BaseSeparationStyle


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
            ctx.focused_idx = max(0, ctx.focused_idx - 1)
        elif key == curses.KEY_DOWN:
            ctx.focused_idx = min(ctx.total_buttons - 1, ctx.focused_idx + 1)
        elif key in (curses.KEY_ENTER, ord('\n'), ord('\r'), ord(' ')):
            ctx.pressed_idx = ctx.focused_idx
        ctx.focused_idx = max(0, min(ctx.focused_idx, ctx.total_buttons - 1))

    def spacing(self):
        _spacing()

    def text(self, text: str, style: BaseTextStyle = None):
        _text(text=text, style=style)

    def separation(self, length: int, style: BaseSeparationStyle = None):
        _separation(length, style=style)

    def button(self, text: str, style: BaseButtonStyle = None) -> bool:
        return _button(text=text, style=style)

    def option(self, text: str, style: BaseOptionStyle = None) -> bool:
        return _option(text=text, style=style)


w = Widgets()
