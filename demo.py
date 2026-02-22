import curses
import time

import cl0ui

from cl0ui.widgets import w

from cl0ui.stylesheets import BaseTextStyle, BaseOptionStyle


class WelcomeTextStyle(BaseTextStyle):
    attr = curses.A_BOLD


class IncrementOptionStyle(BaseOptionStyle):
    focused_fg = 10


class DecrementResetOptionsStyle(BaseOptionStyle):
    focused_fg = 167


counter = 0


def frame():
    global counter

    w.spacing()

    w.text(text="Welcome to [#ITALIC]cl0ui[#RESET] demo!", style=WelcomeTextStyle())
    w.text(text=f"Current time: [#MAGENTA]{time.strftime('%H:%M:%S')}[#RESET]")

    w.spacing()
    w.separation(22)
    w.spacing()

    w.text(text=f"Counter value: [#SKY_BLUE]{counter}[#RESET]")

    w.spacing()

    if w.option(text="+ Increment", style=IncrementOptionStyle()):
        counter += 1

    if w.option(text="- Decrement", style=DecrementResetOptionsStyle()):
        counter -= 1

    w.spacing()
    if w.option(text="# Reset", style=DecrementResetOptionsStyle()):
        counter = 0

    w.spacing()
    w.separation(16)
    w.spacing()

    if w.button(text="Exit"):
        cl0ui.quit()


if __name__ == "__main__":
    cl0ui.run(draw_frame_callback=frame, title="Example Application")
