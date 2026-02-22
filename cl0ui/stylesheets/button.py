import curses


class BaseButtonStyle:
    attr: int = curses.A_NORMAL
    focused_attr: int = curses.A_REVERSE
    padding: int = 2
    fg: int = -1
    bg: int = -1
