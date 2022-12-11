from game.casting.cast import Cast
from game.scripting.script import Script


class Scene:
    def __init__(self, director):
        self.director = director

        self.cast = Cast()
        self.script = Script(director, self.cast)

        self.next_scene = None

    def setup(self):
        # Setup the script, create actors, scene-based state, etc.
        pass

    def tick(self):
        self.script.execute("input")
        self.script.execute("update")
        self.script.execute("output")

    def run(self):
        while self.next_scene is None:
            self.tick()
        return self.next_scene
