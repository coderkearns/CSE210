> How did you apply inheritance to your program's design?

Answer here. Make sure to: (1) answer the question, (2) use code examples, (3) write at least 100 words, and (4) write in paragraph form.

I'm using inheritance as a way to use code as data. The game requires both rock actors and gem actors, which have different score when collected and different "icons". It also requires the usual "robot" actor that a player controls, which does not participate in physics or collectible mechanics.

The inheritance of these implementations looks like so to avoid duplicating code:

`Actor()` contains the usual actor code and even velocity information, but the actual movement and physics are not implemented.

The robots is a simple `Actor()` without any subclass. It is controlled manually by the `Director()`.

Collectible code is implemented in `Collectible()`, which inherits from `Actor()`. It contains the code for usings collectibles but does not contain the specifics of gems and rocks.

There are two respective `Gem()` and `Rock()` classes, which both inherit from `Collectible()`. They don't contain logic, only data about score and visuals. Inheritance allows them to be used anywhere an actor is needed are remove the need to store a `.is_gem` or `.is_rock` state in *every* actor.
