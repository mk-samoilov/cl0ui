import curses


class BaseTextStyle:
    attr: int = curses.A_NORMAL
    fg: int = -1
    bg: int = -1
