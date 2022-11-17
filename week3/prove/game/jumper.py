class Jumper:
    def __init__(self):
        self.strings_left = 5

    def guess_incorrect(self):
        """Subtracts 1 string for guessing incorrectly"""
        self.strings_left -= 1
