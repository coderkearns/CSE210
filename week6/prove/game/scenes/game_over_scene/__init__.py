from game.scenes.scene import Scene

import constants
from game.casting.actor import Actor
from game.shared.point import Point

from game.scripting.actions.draw_actors import DrawActorsAction


class GameOverScene(Scene):
    def setup(self):
        game_over = Actor()
        game_over.set_text("Game Over!")
        game_over.set_position(Point(0, 0))
        self.cast.add_actor("messages", game_over)

        score = Actor()
        score.set_text(f"You had {self.director.points} points!")
        score.set_position(Point(0, 1 * constants.CELL_SIZE))
        self.cast.add_actor("messages", score)

        self.script.add_action("output", DrawActorsAction())

    def tick(self):
        self.script.execute("output")
