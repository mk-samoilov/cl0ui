import curses

_color_pairs: dict = {}
_next_pair: int = 1


def get_color_pair(fg: int, bg: int) -> int:
    global _next_pair
    key = (fg, bg)
    if key not in _color_pairs:
        curses.init_pair(_next_pair, fg, bg)
        _color_pairs[key] = _next_pair
        _next_pair += 1
    return curses.color_pair(_color_pairs[key])


class Context:
    win = None
    row: int = 0
    button_count: int = 0
    focused_idx: int = 0
    pressed_idx = None
    total_buttons: int = 0


ctx = Context()
