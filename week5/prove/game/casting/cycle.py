import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle(Actor):
    def __init__(self, name, starting_position):
        super().__init__()
        self.name = name
        self._trail = []

        self.set_text("@")
        self.set_color(constants.players[self.name])
        self.set_position(starting_position)

    def get_trail(self):
        return self._trail

    def move_next(self):
        old_position = self.get_position()

        # move self
        super().move_next()

        # create new trail at old position
        trail = Actor()
        trail.set_text("#")
        trail.set_color(self.get_color())
        trail.set_position(old_position)
        self._trail.append(trail)
