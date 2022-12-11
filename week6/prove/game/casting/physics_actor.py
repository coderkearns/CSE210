from .actor import Actor

import constants
from game.shared.point import Point


class PhysicsActor(Actor):
    def __init__(self, speed=1):
        super().__init__()

        self._velocity = Point(0, speed)

    def move_next(self):
        self._position = self._position.add(self._velocity.scale(constants.CELL_SIZE))
        if self._position._y > constants.MAX_Y:
            self._position._y = constants.MAX_Y
