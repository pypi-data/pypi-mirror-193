import numpy as np
from Xlib import display as disp
from Xlib import X
from .utils.itr import extract_text
from ..display.panel import Panel
from ..display.screen import Screen
from ..display.utils.element import find_element, find_elements


def display_handler(f):
    def wrapper(*args):
        try:
            return f(*args)
        finally:
            args[0]._dsp.close()

    return wrapper


class Display:
    screens = []

    def __init__(self):
        self.panel = Panel()
        self.screens.append(Screen(display=self, number=0))  # todo: xdotool get all screens
        self.current_screen = self.screens[0]

    def screen(self, number):
        return [i for i in self.screens if i.number == number][0]

    @property
    @display_handler
    def width(self):
        scr = self._dsp.screen()
        width = scr.width_in_pixels
        return width

    @property
    @display_handler
    def height(self):
        scr = self._dsp.screen()
        height = scr.height_in_pixels
        return height

    @display_handler
    def screenshot(self, x=0, y=0, width=None, height=None):
        scr = self._dsp.screen()
        width = width if width else scr.width_in_pixels
        height = height if height else scr.height_in_pixels
        root = scr.root
        raw = root.get_image(x, y, width, height, X.ZPixmap, 0xffffffff)
        bgr_data = np.frombuffer(raw.data, dtype=np.uint8).reshape((height, width, 4))[:, :, :3]
        # rgb_data = bgr_data[..., ::-1]
        return bgr_data

    @staticmethod
    def find_element(template, screenshot, threshold=.85):
        return find_element(str(template), screenshot, threshold=threshold)

    @staticmethod
    def find_elements(template, screanshot, threshold=.9):
        return find_elements(str(template), screanshot, threshold=threshold)

    @staticmethod
    def read_text(image, left_top=None, right_bottom=None):
        return extract_text(image, left_top, right_bottom)

    @property
    def _dsp(self):
        self.__dsp = disp.Display()
        return self.__dsp
