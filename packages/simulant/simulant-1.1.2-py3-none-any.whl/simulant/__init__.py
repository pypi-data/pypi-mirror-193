import sys
import time

import pytesseract

from .display import Display
from .keyboard import Keyboard
from .keyboard.key import keys
from .mouse import Mouse
from .os import Shell

__all__ = ['sm', 'keys']


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class BaseSimulant(metaclass=Singleton):
    def __init__(self):
        self.os = sys.platform
        self.keyboard = Keyboard()
        self.display = Display()
        self.mouse = Mouse()

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"<Simulant: {self.os}>"


def wait(f):
    def wrapper(*args, **kwargs):
        self = args[0]
        wait_arg = kwargs.get('wait')
        if wait_arg is None:
            return f(*args, **kwargs)
        else:
            wait_arg = kwargs.pop('wait')
            start = time.time()
            result = None
            while time.time() - start <= wait_arg and result is None:
                result = f(*args, **kwargs)
                if not result:
                    time.sleep(.2)
            return result

    return wrapper


class Simulant(Shell, BaseSimulant):

    def copy_to_clipboard_and_get_text(self):
        self.execute(f'echo "empty" | xclip', output=False)
        self.keyboard.key(keys.CTRL + 'a')
        self.keyboard.key(keys.CTRL + 'c')
        self.keyboard.key(keys.ESC)
        text = self.clipboard
        if text == 'empty':
            return ''
        else:
            return text

    def paste_text(self, text):
        self.clipboard = text
        self.keyboard.key(keys.CTRL + 'v')

    @property
    def clipboard(self):
        return self.execute("xclip -o")

    @clipboard.setter
    def clipboard(self, value):
        self.execute(f'echo "{value}" | xclip -i -selection clipboard', output=False)

    @wait
    def get_window_by_id(self, window_id):
        return self.display.screen(0).get_window_by_id(window_id)

    @wait
    def get_window_by_name(self, window_name, regex=True):
        return self.display.screen(0).get_window_by_name(window_name, regex=regex)

    def screenshot(self, position_x=0, position_y=0, width=None, height=None):
        return self.display.screenshot(position_x, position_y, width, height)

    def read_text(self, position_x, position_y, width, height):
        image = self.screenshot(position_x, position_y, width, height)
        string = pytesseract.image_to_string(image)
        return string


sm = Simulant()
