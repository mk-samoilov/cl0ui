import curses


class BaseAppStyle:
    smoothed_frame: bool = False
    frame_attr: int = curses.A_NORMAL
    frame_fg: int = -1
    frame_bg: int = -1
    title_attr: int = curses.A_BOLD
    title_fg: int = -1
    title_bg: int = -1
