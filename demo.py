import curses
import time

import cl0ui

from cl0ui.widgets import w

from cl0ui.stylesheets import BaseAppStyle, BaseTextStyle, BaseOptionStyle, BaseButtonStyle


class TitleStyle(BaseTextStyle):
    attr = curses.A_BOLD
    fg = curses.COLOR_CYAN


class IncrementStyle(BaseOptionStyle):
    focused_fg = 119
    focused_attr = curses.A_NORMAL


class DecrementStyle(BaseOptionStyle):
    focused_fg = 167
    focused_attr = curses.A_NORMAL


class ResetStyle(BaseOptionStyle):
    focused_fg = 167
    focused_attr = curses.A_REVERSE


class ExitButtonStyle(BaseButtonStyle):
    focused_fg = 167
    focused_attr = curses.A_NORMAL


counter = 0


def frame():
    global counter

    w.spacing()

    w.text(text="Welcome to [#ITALIC]cl0ui[#RESET] library Demo!", style=TitleStyle())
    w.text(text="You can navigate in interface using arrow keys on keyboard.")

    w.spacing()

    w.text(text=f"[#GRAY]- [#GOLD]Time:[#RESET] [#MAGENTA]{time.strftime('%H:%M:%S')}[#RESET] ")
    w.text(text=f"[#GRAY]- [#GOLD]Date:[#RESET] [#BRIGHT_BLUE]{time.strftime('%d.%m.%Y')}[#RESET]")

    w.spacing()
    w.separation(20)
    w.spacing()

    if counter > 0:
        counter_color = "#BRIGHT_GREEN"
    elif counter < 0:
        counter_color = "#BRIGHT_RED"
    else:
        counter_color = "#GRAY"

    w.text(text=f"Counter: [{counter_color}]{counter if counter == 0 else f'{counter:+d}'}[#RESET]")

    w.spacing()

    if w.option(text="+ Increment", style=IncrementStyle()):
        counter += 1

    if w.option(text="- Decrement", style=DecrementStyle()):
        counter -= 1

    w.spacing()

    if w.option(text="# Reset", style=ResetStyle()):
        counter = 0

    w.spacing()
    w.separation(16)
    w.spacing()

    if w.button(text="Quit", style=ExitButtonStyle()):
        cl0ui.quit()


class AppStyle(BaseAppStyle):
    smoothed_frame = True
    # frame_fg = curses.COLOR_CYAN
    # title_fg = curses.COLOR_CYAN


if __name__ == "__main__":
    cl0ui.run(draw_frame_callback=frame, title="cl0ui Demo #1", style=AppStyle())
