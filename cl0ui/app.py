import curses
from typing import Callable

from cl0ui.widgets import w
from cl0ui.widgets._ctx import get_color_pair
from cl0ui.stylesheets.app import BaseAppStyle

_running = False


def quit_app():
    global _running
    _running = False


class Application:
    def __init__(self, draw_frame_callback: Callable, title: str = "cl0ui", style: BaseAppStyle = None):
        self._callback = draw_frame_callback
        self._title = title
        self._style = style or BaseAppStyle()

    def run(self):
        curses.wrapper(self._main)

    def _draw_border(self, stdscr):
        s = self._style
        h, cols = stdscr.getmaxyx()

        if s.smoothed_frame:
            tl, tr, bl, br = '\u256d', '\u256e', '\u2570', '\u256f'
        else:
            tl, tr, bl, br = '\u250c', '\u2510', '\u2514', '\u2518'
        hz, vt = '\u2500', '\u2502'

        frame_attr = s.frame_attr
        if s.frame_fg != -1 or s.frame_bg != -1:
            frame_attr |= get_color_pair(s.frame_fg, s.frame_bg)

        title_attr = s.title_attr
        if s.title_fg != -1 or s.title_bg != -1:
            title_attr |= get_color_pair(s.title_fg, s.title_bg)

        title = f' {self._title} '
        fill = cols - len(title) - 3
        top_left  = tl + hz
        top_right = hz * fill + tr

        try:
            stdscr.addstr(0, 0, top_left, frame_attr)
            stdscr.addstr(0, 2, title, title_attr)
            stdscr.addstr(0, 2 + len(title), top_right, frame_attr)
        except curses.error:
            pass

        for row in range(1, h - 1):
            try:
                stdscr.addstr(row, 0, vt, frame_attr)
                stdscr.addstr(row, cols - 1, vt, frame_attr)
            except curses.error:
                pass

        bottom = bl + hz * (cols - 2) + br
        try:
            stdscr.addstr(h - 1, 0, bottom[:-1], frame_attr)
            stdscr.insstr(h - 1, cols - 1, br, frame_attr)
        except curses.error:
            pass

    def _main(self, stdscr):
        global _running
        _running = True

        curses.curs_set(0)
        curses.start_color()
        curses.use_default_colors()
        stdscr.timeout(100)

        w._attach(stdscr)

        while _running:
            stdscr.erase()
            self._draw_border(stdscr)

            w._begin_frame(start_row=1)
            self._callback()
            w._end_frame()

            stdscr.refresh()

            key = stdscr.getch()
            if key != -1:
                w._handle_key(key)
