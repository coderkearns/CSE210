import constants

from game.casting.actor import Actor

from game.shared.point import Point

BOTTOM = constants.MAX_Y - constants.CELL_SIZE


class PlayerActor(Actor):
    def __init__(self):
        super().__init__()
        self.set_text(constants.PLAYER_ICON)
        self.set_color(constants.PLAYER_COLOR)
        self.set_position(Point(0, BOTTOM))
