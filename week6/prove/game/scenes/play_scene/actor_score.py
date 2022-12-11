from game.casting.message_actor import MessageActor

import constants
from game.shared.point import Point

CENTER_X = int(constants.MAX_X / 2)


class ScoreActor(MessageActor):
    def __init__(self):
        super().__init__("Score: 0", Point(CENTER_X, 0))

        self._points = 0
        self.add_points(0)

    def add_points(self, points):
        self._points += points
        self.set_text(f"Score: {self._points}")

    def get_points(self):
        return self._points
