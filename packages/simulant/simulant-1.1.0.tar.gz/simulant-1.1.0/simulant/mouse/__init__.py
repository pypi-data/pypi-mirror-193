import re
import subprocess
from ..os import Shell
from .human import wind_mouse


class Center(Shell):
    def click(self):
        self.execute("xdotool click --clearmodifiers 2")


class Right(Shell):
    def click(self):
        self.execute("xdotool click --clearmodifiers 3")


class Mouse(Shell):

    def __init__(self):
        self.center = Center()
        self.right = Right()

    @property
    def current_position(self):
        current = subprocess.check_output(["xdotool", "getmouselocation"]).decode('utf-8')
        x, y = re.findall(r'x:(\d+) y:(\d+) ', current)[0]
        return {"x": int(x), "y": int(y)}

    def _move(self, x, y):
        self.execute(f"xdotool mousemove --clearmodifiers --sync {x} {y}")

    def move(self, x, y, fast=False):
        current = self.current_position
        if fast:
            self._move(x, y)
        else:
            wind_mouse(*current.values(), x, y, move_mouse=self._move)

    def click(self):
        self.execute("xdotool click --clearmodifiers 1")
