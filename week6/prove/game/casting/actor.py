import constants

from game.shared.color import Color
from game.shared.point import Point


class Actor:
    def __init__(self):
        self._text = ""
        self._font_size = constants.FONT_SIZE
        self._color = Color(255, 255, 255)
        self._position = Point(0, 0)

        self._is_centered = False

    def get_color(self):
        return self._color

    def get_font_size(self):
        return self._font_size

    def get_position(self):
        return self._position

    def get_text(self):
        return self._text

    def get_is_centered(self):
        return self._is_centered

    def set_color(self, color):
        self._color = color

    def set_position(self, position):
        self._position = position

    def set_font_size(self, font_size):
        self._font_size = font_size

    def set_text(self, text):
        self._text = text

    def set_is_centered(self, is_centered):
        self._is_centered = is_centered

    def move_next(self):
        """Changes the current position to the next postilion. Actors don't move by default."""
        pass
