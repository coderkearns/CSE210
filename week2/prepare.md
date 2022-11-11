> What is abstraction and why is it important?

Abstraction refers to "hiding" complex implementation details of a system behind a (simpler) interface. It is very important to working at any kind of high level, as without we would need to manually control every detail of our code at the transistor level.

Is our code, we are abstracting the random generator `random.randint(1, 6)` behind a `Die` class, which also handles the point calculations, all using `Die().roll()`.
