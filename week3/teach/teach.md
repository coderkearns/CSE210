> How did you apply encapsulation to your program's design?

Encapsulation was used to separate the pieces of game state into separate classes. We determined we needed state to store the secret word, the guessed letters, and the number of strings remaining.

They were divided into their separate classes:

The `Jumper` class stores the `strings_left` state and had a `guess_incorrect()` method that lowers it by 1 each the an incorrect guess was made.

The `Word` class randomly chose and stored the `secret_word` state, and a list of all `guessed_letters`. It provided methods to check whether a letter was in the word (`is_correct_letter`), to add guessed letters (`add_letter`), and an `is_guessed` variable holding whether the *entire* word had been guessed.

In order to keep all terminal interaction separate from cluttering up the `Director` class, we have a `Console` class for handling the input and output, including input validation. It also included the `output_jumper()` method to show the icon representing the current `strings_left` state.
