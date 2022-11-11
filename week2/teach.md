> How did you apply abstraction in your program's design?

There are multiple abstractions in my implementation of HiLo. Instead of manually calling `random.randint()` twice and comparing the two, there is a `Card` class that does it automatically, and has `was_higher()` and `was_lower()` methods to abstract the comparisons.

The `Director` class also abstracts away the game loop and functions into a simple `Director().play()` interface.
