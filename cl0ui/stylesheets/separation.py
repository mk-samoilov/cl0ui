import curses


class BaseSeparationStyle:
    attr: int = curses.A_NORMAL
    char: str = '\u2500'
    fg: int = -1
    bg: int = -1
