> How did you ensure maintainability in your program's design?

Answer here. Make sure to: (1) answer the question, (2) use code examples, (3) write at least 100 words, and (4) write in paragraph form.

I ensured maintainability in my code using three philosophies:

First, I made sure I kept all logic organized with similar logic. Because there were three scenes in this game, actions and actions that were not re-used were kept with their respective scene insntead of globally. Example: I stored the `PlayerActor` in a `actor_player.py` inside the "play_scene" folder instead of the "casting" folder, because it was only used in the play scene. Actions were similar, except that I put global actions like `DrawActorsAction` inside the "scripting" folder because they were re-used.

Second, I used modular design to make it easy to track down bugs. Rather than attempting to keep all the logic for each scene on its own, they all use `Script`s and `Cast`s like in previous games to find bugs quickly.

Lastly, I used stored globals well. At the beginning I has a couple issues with global values. I changed this and stored almost all the globals in `constants.py` to make it simple to change in multiple places.
