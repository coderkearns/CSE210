from .actor import Actor

from game.shared.point import Point


class MessageActor(Actor):
    def __init__(self, text, position=Point(0, 0)):
        super().__init__()

        self.set_text(text)
        self.set_position(position)
        self.set_is_centered(True)
