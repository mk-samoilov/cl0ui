import curses

from typing import Callable

from cl0ui.widgets import w


_running = False


def quit_app():
    global _running
    _running = False


class Application:
    def __init__(self, draw_frame_callback: Callable, title: str = "cl0ui"):
        self._callback = draw_frame_callback
        self._title = title

    def run(self):
        curses.wrapper(self._main)

    def _draw_border(self, stdscr):
        h, cols = stdscr.getmaxyx()

        title = f' {self._title} '
        fill = cols - len(title) - 3
        top = '\u250c\u2500' + title + '\u2500' * fill + '\u2510'
        try:
            stdscr.addstr(0, 0, top)
        except curses.error:
            pass

        for row in range(1, h - 1):
            try:
                stdscr.addstr(row, 0, '\u2502')
            except curses.error:
                pass
            try:
                stdscr.addstr(row, cols - 1, '\u2502')
            except curses.error:
                pass

        bottom = '\u2514' + '\u2500' * (cols - 2) + '\u2518'
        try:
            stdscr.addstr(h - 1, 0, bottom[:-1])
            stdscr.insstr(h - 1, cols - 1, '\u2518')
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
