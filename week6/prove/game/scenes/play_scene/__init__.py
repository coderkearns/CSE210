from game.scenes.scene import Scene

from .actor_score import ScoreActor
from .actor_player import PlayerActor

from .action_move_player import MovePlayerAction
from .action_update_score import UpdateScoreAction
from .action_move_rocks import MoveRocksAction
from .action_generate_rock import GenerateRockAction
from .action_handle_collisions import HandleCollisionsAction
from game.scripting.actions.draw_actors import DrawActorsAction


class PlayScene(Scene):
    def setup(self):
        self.cast.add_actor("players", PlayerActor())
        self.cast.add_actor("score", ScoreActor())

        self.script.add_action("input", MovePlayerAction())
        self.script.add_action("update", UpdateScoreAction())
        self.script.add_action("update", MoveRocksAction())
        self.script.add_action("update", GenerateRockAction())
        self.script.add_action("update", HandleCollisionsAction())
        self.script.add_action("output", DrawActorsAction())

    def tick(self):
        self.script.execute("input")
        self.script.execute("update")
        self.script.execute("output")
