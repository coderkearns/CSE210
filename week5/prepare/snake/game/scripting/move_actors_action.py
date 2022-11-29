from game.scripting.action import Action


class MoveActorsAction(Action):
    def execute(self, cast, script):
        for actor in cast.get_all_actors():
            actor.move_next()
