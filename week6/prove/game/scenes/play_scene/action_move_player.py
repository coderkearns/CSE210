from game.scripting.action import Action

import constants
from game.shared.point import Point

BOTTOM = constants.MAX_Y - constants.CELL_SIZE
RIGHT = constants.MAX_X - constants.CELL_SIZE


class MovePlayerAction(Action):
    def execute(self, director, cast, script):
        player = cast.get_nth_actor("players", 0)

        velocity = Point(0, 0)

        # Drop if not touching ground
        if player.get_position().get_y() != BOTTOM:
            velocity = velocity.add(Point(0, 1))
        else:
            # Jump if "W" is pressed
            if director.keyboard_service.is_key_down("KEY_W"):
                velocity = velocity.add(Point(0, -5))

        # Go left if "A" is pressed
        if (
            director.keyboard_service.is_key_down("KEY_A")
            and player.get_position().get_x() > 0
        ):
            velocity = velocity.add(Point(-1, 0))

        # Go right if "D" is pressed
        if (
            director.keyboard_service.is_key_down("KEY_D")
            and player.get_position().get_x() < RIGHT
        ):
            velocity = velocity.add(Point(1, 0))

        player.set_position(
            player.get_position().add(velocity.scale(constants.CELL_SIZE))
        )
