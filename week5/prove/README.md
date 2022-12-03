# Cycle

## Description

Cycle is a game where the players try to cut each other off using cycles that leave a trail behind them.

## Controls

- Player One is **RED**, and controls using *WSAD*.
- Player Two is **BLUE** and controls using *IJKL*

## Project Structure

```
prove/
├── constants.py
├── game/
│   ├── casting/
│   │   ├── actor.py
│   │   ├── cast.py
│   │   ├── cycle.py
│   │   └── score.py
│   ├── directing/
│   │   └── director.py
│   ├── scripting/
│   │   ├── action.py
│   │   ├── control_actors_action.py
│   │   ├── draw_actors_action.py
│   │   ├── handle_collisions_action.py
│   │   ├── move_actors_action.py
│   │   └── script.py
│   ├── services/
│   │   ├── keyboard_service.py
│   │   └── video_service.py
│   └── shared/
│       ├── color.py
│       └── point.py
├── __main__.py
└── README.md
```

## Dependencies

- Raylib

## Author

Carter Kearns (coder.kearns@gmail.com)
