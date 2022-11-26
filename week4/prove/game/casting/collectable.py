import random

from game.casting.actor import Actor
from game.shared.point import Point


class Collectable(Actor):
    score = 0
    text = ""

    def __init__(self):
        super()
        self.set_velocity(Point(0, random.randint(1, 3)))


class Gem(Collectable):
    score = 1
    text = "*"


class Rock(Collectable):
    score = -1
    text = "o"
