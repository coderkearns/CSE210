> What is inheritance and why is it important?

Inheritance allows you to re-use the same abstraction and code for a sort of sub-model of itself. In Python, this means a class can "inherit" from another class and act as both. It keep all methods and properties from the previous class, excepting those that are overridden. In addition, the classes from the "smaller" class are also kept for *only* its members.

As an example, we used the `Actor` class and the `Artifact` class. `Artifact` inherits from `Actor`, so we can use an `Artifact()` instance anywhere an `Actor` is needed, but it also has additional properties. We render `Actor()`s, but we can use the same method to render `Artifact()`s.
