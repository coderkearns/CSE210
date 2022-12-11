import constants

from game.casting.physics_actor import PhysicsActor


class RockActor(PhysicsActor):
    def __init__(self, position):
        super().__init__(constants.ROCK_FALL_SPEED)
        self.set_text(constants.ROCK_ICON)
        self.set_color(constants.ROCK_COLOR)
        self.set_position(position)
