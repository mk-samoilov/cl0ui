import curses


class BaseOptionStyle:
    attr: int = curses.A_NORMAL
    focused_attr: int = curses.A_REVERSE
    fg: int = -1
    bg: int = -1
    focused_fg: int = -1
    focused_bg: int = -1
