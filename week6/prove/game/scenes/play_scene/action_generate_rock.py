import random

from game.scripting.action import Action

import constants
from game.shared.point import Point
from .actor_rock import RockActor


class GenerateRockAction(Action):
    def execute(self, director, cast, script):
        if random.random() <= constants.ROCK_SPAWN_CHANCE:
            x = (
                random.randint(0, int(constants.MAX_X / constants.CELL_SIZE))
                * constants.CELL_SIZE
            )
            rock = RockActor(Point(x, 0))
            cast.add_actor("rocks", rock)
