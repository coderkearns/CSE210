from game.scripting.action import Action

class UpdateScoreAction(Action):
    def execute(self, director, cast, script):
        score = cast.get_nth_actor("score", 0)
        score.add_points(1)
