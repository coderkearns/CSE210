from game.scripting.action import Action

import constants

class MoveRocksAction(Action):
    def execute(self, director, cast, script):
        rocks = cast.get_actors("rocks")

        for rock in rocks:
            rock.move_next()

            if rock.get_position().get_y() > constants.MAX_Y:
                cast.remove_actor("rocks", rock)
