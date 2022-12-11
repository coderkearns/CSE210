import random

from game.scripting.action import Action

import constants
from game.shared.point import Point
from .actor_rock import RockActor


class GenerateRockAction(Action):
    def execute(self, director, cast, script):
        # TODO place this whole code inside an "if random.randint(0, 10) > 5:" etc. to make less rocks?
        x = (
            random.randint(0, int(constants.MAX_X / constants.CELL_SIZE))
            * constants.CELL_SIZE
        )
        rock = RockActor(Point(x, 0))
        cast.add_actor("rocks", rock)
