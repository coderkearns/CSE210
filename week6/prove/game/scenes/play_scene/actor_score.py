from game.casting.actor import Actor

from game.shared.point import Point


class ScoreActor(Actor):
    def __init__(self):
        super().__init__()
        self.set_position(Point(0, 0))

        self._points = 0
        self.add_points(0)

    def add_points(self, points):
        self._points += points
        self.set_text(f"Score: {self._points}")

    def get_points(self):
        return self._points
