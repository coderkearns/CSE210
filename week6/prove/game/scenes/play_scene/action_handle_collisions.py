from game.scripting.action import Action

import constants


class HandleCollisionsAction(Action):
    def execute(self, director, cast, script):
        score = cast.get_nth_actor("score", 0)
        player = cast.get_nth_actor("players", 0)
        rocks = cast.get_actors("rocks")

        for rock in rocks:
            if player.get_position().equals(rock.get_position()):
                director.points = score.get_points()
                director.current_scene.next_scene = "game_over"
                break
