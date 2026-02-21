import time

import cl0ui

from cl0ui.widgets import w


counter = 0


def frame():
    global counter

    w.spacing()

    w.text(text="Hello from cl0ui!")
    w.text(text=f"Current time: {time.strftime('%H:%M:%S')}")

    w.spacing()
    w.separation(22)
    w.spacing()

    w.text(text=f"Counter: {counter}")

    w.spacing()

    if w.button(text="+ Counter"):
        counter += 1

    if w.button(text="- Counter"):
        counter -= 1

    w.spacing()
    w.separation(16)
    w.spacing()

    if w.button(text="Exit"):
        cl0ui.quit()


if __name__ == "__main__":
    cl0ui.run(draw_frame_callback=frame, title="Example Application")
