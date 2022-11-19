from game.jumper import Jumper
from game.word import Word
from game.console import Console


class Director:
    def __init__(self):
        self._word = Word()
        self._console = Console()
        self._jumper = Jumper()

        self.current_guess = ""

    def start_game(self):
        while True:
            self.do_outputs()

            if self.is_game_over():
                self.do_finish()
                break

            self.do_inputs()
            self.do_updates()

    def do_outputs(self):
        self._console.output_word(self._word)
        self._console.output_jumper(self._jumper.strings_left)

    def do_inputs(self):
        self.current_guess = self._console.input_letter()

    def do_updates(self):
        self._word.add_letter(self.current_guess)
        if not self._word.is_correct_letter(self.current_guess):
            self._jumper.guess_incorrect()

    def is_game_over(self):
        """Returns True if the game is over, either by winning or running out of strings, False otherwise"""
        return (self._jumper.strings_left == 0) or (self._word.is_guessed)

    def do_finish(self):
        """Prints a message depending on whether the user won of lost"""
        if self._jumper.strings_left == 0:
            # Lose ending
            self._console.output("Game over!")
        else:
            # Win ending
            self._console.output("You guessed it and saved the jumper!")
