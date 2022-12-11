from game.scenes.scene import Scene

import constants

from game.casting.message_actor import MessageActor
from game.shared.point import Point

from game.scripting.actions.draw_actors import DrawActorsAction

CENTER_X = int(constants.MAX_X / 2)


class MainScene(Scene):
    def setup(self):
        self.cast.add_actor(
            "messages", MessageActor("Welcome to Rock Dodge!", Point(CENTER_X, 15 * 5))
        )
        self.cast.add_actor(
            "messages",
            MessageActor("Use the WASD keys to move.", Point(CENTER_X, 15 * 7)),
        )
        self.cast.add_actor(
            "messages",
            MessageActor(
                "Survive without hitting a rock as long as possible!",
                Point(CENTER_X, 15 * 8),
            ),
        )
        self.cast.add_actor(
            "messages", MessageActor("Press ENTER to start", Point(CENTER_X, 15 * 10))
        )

        self.script.add_action("output", DrawActorsAction())

    def tick(self):
        if self.director.keyboard_service.is_key_down("KEY_ENTER"):
            self.next_scene = "play"

        self.script.execute("output")
