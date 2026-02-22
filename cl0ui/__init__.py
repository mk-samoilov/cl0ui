from typing import Callable

from .app import Application, quit_app as quit
from .stylesheets.app import BaseAppStyle


def run(draw_frame_callback: Callable, title: str, style: BaseAppStyle = None):
    Application(draw_frame_callback=draw_frame_callback, title=title, style=style).run()


__all__ = ["run", "quit"]
