import random


class Card:
    def __init__(self):
        self.value = 0

    def draw(self):
        self.value = random.randint(1, 13)

    def is_higher_than(self, other):
        return self.value >= other.value
