from ..display.window import Window
from ..os import Shell, ExecuteException


class Screen(Shell):
    def __init__(self, display, number):
        self._display = display
        self.number = number

    @property
    def focus_window(self):
        return Window(self, self.execute('xdotool getactivewindow'))

    def get_window_by_id(self, window_id):
        try:
            return Window(self, window_id)
        except ExecuteException:
            return None

    def get_window_by_name(self, window_name, regex=True):
        if not regex:
            window_name = window_name.replace('.', '\.').replace('^', '\^').replace('$', '\$').replace('*', '\*').replace('(', '\(').replace(')', '\)').replace('?', '\?').replace('+', '\+')
        try:
            window_id = self.execute(f"xdotool search --name '{window_name}'")
            return Window(self, window_id)
        except ExecuteException:
            return None

    def get_windows(self, class_name):
        windows_ids = self.execute(f"xdotool search --classname --onlyvisible {class_name}")
        if type(windows_ids) == int:
            windows_ids = [windows_ids]
        windows_obj = [Window(self, window_id) for window_id in windows_ids]
        return windows_obj

    @staticmethod
    def is_select():  # todo check xdotool
        return True

    def __str__(self):
        return f"<{self.__class__.__name__}: {self.number}>"

    def __repr__(self):
        return self.__str__()
