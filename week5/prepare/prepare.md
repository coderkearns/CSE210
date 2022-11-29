> What is polymorphism and why is it important?

Polymorphism is the concept that sub-types of a type can be used wherever the base type is used. This does not apply in reverse, however. An example could be a case with a `Animal()` class, with the subtypes of `WaterAnimal()` and `LandAnimal()`. A function like `look_for_animal(animal)` could take *any* Animal as its argument, so you could pass a water animal to the function and it would still work. A more specific example like `fish_for_animal(water_animal)`, however, would only be able to use WaterAnimals and their subtypes.

Polymorphism is so important because it allows us to re-use code and abstractions with multiple use cases.

In the Snake game, we have a common `Actor()` class and subtypes `Food()` and `Snake()`. They both are used anywhere actors are used (checking for collisions, rendering, etc.) but also have their own specific code and logic like special movement for the snake and points for the food.
