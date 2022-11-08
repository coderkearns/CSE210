import random

POINTS_TABLE = {1: 100, 5: 50}


class Die:
    """A small cube with a different number of spots on each of its six sides.

    The responsibility of Die is to keep track of the side facing up and calculate the points for
    it.

    Attributes:
        value (int): The number of spots on the side facing up.
        points (int): The number of points the die is worth.
    """

    def __init__(self, sides=6):
        """Constructs a new instance of Die with a value and points attribute.

        Args:
            self (Die): An instance of Die.
            sides (int): The number of sides
        """
        self.sides = sides

        self.value = 0
        self.points = 0

    def roll(self):
        """Generates a new random value and calculates the points.

        Args:
            self (Die): An instance of Die.
        """
        self.value = random.randint(1, self.sides)
        self.points = POINTS_TABLE.get(self.value, 0)
