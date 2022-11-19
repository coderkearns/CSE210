from game.parachute import output_parachute

LETTERS = "abcdefghijklmnopqrstuvwxyz"


class Console:
    def output(self, msg):
        """Output a message to the console"""
        print(msg)

    def output_word(self, word):
        """Output the secret word, replacing each letter that has not yet been guessed with _"""
        print(word.string_representation())

    def output_jumper(self, strings_left):
        """Show the parachute icon based on the number of strings left"""
        output_parachute(strings_left)

    def input_letter(self):
        """Get the user to input a letter. Letters are lowercased automatically, and it ensures that the user inputs a real letter, re-asking if they do not."""
        inp = "_"
        while inp not in LETTERS:
            inp = input("Guess a letter [a-z]: ").strip().lower()
        return inp
