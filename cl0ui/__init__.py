from typing import Callable

from .app import Application, quit_app as quit


def run(draw_frame_callback: Callable, title: str):
    Application(draw_frame_callback=draw_frame_callback, title=title).run()


__all__ = ["run", "quit"]
