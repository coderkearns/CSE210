> What is a version control system and why is it important?

Version control systems save code and allow changes to be made incrementally to separate parts of the code. When developing on your own, this is useful as a "history" tool, allowing you to view and revert back to your previous changes.

It becomes even more useful when used in a team. Multiple people can change different parts of the code without worrying about overwriting other's work. Multiple people can work on the same piece of code and merge those changes together without fear of breaking things.

Example:

Two developers are both working on a simple tic-tac-toe game. In one file `constants.py` there is a `PLAYER_1_CONST = "X"` and `PLAYER_2_CONST = "O"`. In another file called `ai.py` there is a function for controlling the AI player.

The first developer decided they want to use "*" and "#" instead of "X" and "O", so they change the `constants.py` file. They then use `$ git add constants.py` and `$ git commit -m 'Change constants to * and #'`.

At the same time, the other developer is changing the AI code so the AI always tries to get the corner slots first. They use `$ git add ai.py` and `$ git commit -m 'Change AI code to prioritize corners'`.

While it could be tricky because Developer 1 still has the old `ai.py` and Developer 2 still has the old `constants.py`, they don't need to worry because they used version control. When they both run `$ git push`, GitHub will see that they made different changes and can easily merge them without worry. It even keeps a record of everything they did, complete with their commit messages on what and why they changes their respective files!
