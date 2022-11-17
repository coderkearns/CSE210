import random

WORDS = [
    "energetic",
    "teaching",
    "motionless",
    "skinny",
    "cool",
    "wise",
    "condition",
    "axiom",
    "difficult",
    "bagpipes",
    "rural",
    "banjo",
    "remember",
    "beekeeper",
    "cumbersome",
    "blitz",
    "blizzard",
    "fruit",
    "bookworm",
    "oven",
    "boxful",
    "finger",
    "buffalo",
    "trot",
    "past",
    "reign",
    "buzzing",
    "fax",
    "argument",
    "broad",
    "flight",
    "croquet",
    "crypt",
    "flavor",
    "cycle",
    "political",
    "soak",
    "disavow",
    "divide",
    "duplex",
    "dwarves",
    "sister",
    "equip",
    "allow",
    "kind",
    "instrument",
    "plane",
    "jumpy",
    "economic",
    "pleasure",
    "madly",
    "good",
    "stir",
    "night",
    "relax",
    "reflect",
]


class Word:
    def __init__(self):
        self.secret_word = random.choice(WORDS)

        self.guessed_letters = []
        self.is_guessed = False

    def add_letter(self, letter):
        """Adds a letter to the list of guesses, then checks to see if the entire word has been guessed."""
        self.guessed_letters.append(letter)

        self.is_guessed = False not in [
            letter in self.guessed_letters for letter in self.secret_word
        ]

    def is_correct_letter(self, letter):
        """Returns True if the given letter is in the secret word"""
        return letter in self.secret_word
