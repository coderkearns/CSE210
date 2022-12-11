import pyray


class KeyboardService:
    def is_key_up(self, key):
        return pyray.is_key_up(getattr(pyray, key))

    def is_key_down(self, key):
        return pyray.is_key_down(getattr(pyray, key))
