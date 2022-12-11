from game.scenes.scene import Scene

from game.casting.actor import Actor
from game.shared.point import Point

from game.scripting.actions.draw_actors import DrawActorsAction


class MainScene(Scene):
    def setup(self):
        actor = Actor()
        actor.set_text("Press enter to start")
        actor.set_position(Point(0, 0))
        self.cast.add_actor("messages", actor)

        self.script.add_action("output", DrawActorsAction())

    def tick(self):
        if self.director.keyboard_service.is_key_down("KEY_ENTER"):
            self.next_scene = "play"

        self.script.execute("output")
