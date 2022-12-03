import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.

    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_trail_collision(cast)
            self._handle_game_over(cast)

    def _handle_trail_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycle1, cycle2 = cast.get_actors("cycles")
        trail1 = cycle1.get_trail()
        trail2 = cycle2.get_trail()

        for t in trail1:
            if cycle2.get_position().equals(t.get_position()):
                self._is_game_over = True
                [
                    score
                    for score in cast.get_actors("scores")
                    if score.name == cycle1.name
                ][0].add_points(1)

        for t in trail2:
            if cycle1.get_position().equals(t.get_position()):
                self._is_game_over = True
                [
                    score
                    for score in cast.get_actors("scores")
                    if score.name == cycle2.name
                ][0].add_points(1)

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cycle1, cycle2 = cast.get_actors("cycles")
            trail1, trail2 = cycle1.get_trail(), cycle2.get_trail()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for actor in [cycle1, cycle2]:
                actor.set_color(constants.WHITE)

            for trail in [trail1, trail2]:
                for actor in trail:
                    actor.set_color(constants.WHITE)
