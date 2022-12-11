# Final Project: Rockk Dodge

## Description

Rock Dodge is a game where you attempt to avoid randomly falling rocks and attempt to survive as long s possible.

## Project Structure

```
prove/
├── game/
│   ├── casting/
│   │   ├── actor.py
│   │   ├── cast.py
│   │   └── physics_actor.py
│   ├── director.py
│   ├── scenes/
│   │   ├── game_over_scene/
│   │   │   └── __init__.py
│   │   ├── main_scene/
│   │   │   └── __init__.py
│   │   ├── play_scene/
│   │   │   ├── action_generate_rock.py
│   │   │   ├── action_handle_collisions.py
│   │   │   ├── action_move_player.py
│   │   │   ├── action_move_rocks.py
│   │   │   ├── action_update_score.py
│   │   │   ├── actor_player.py
│   │   │   ├── actor_rock.py
│   │   │   ├── actor_score.py
│   │   │   └── __init__.py
│   │   └── scene.py
│   ├── scripting/
│   │   ├── action.py
│   │   ├── actions/
│   │   │   └── draw_actors.py
│   │   └── script.py
│   ├── services/
│   │   ├── keyboard_service.py
│   │   └── video_service.py
│   └── shared/
│       ├── color.py
│       └── point.py
├── constants.py
├── __main__.py
└── README.md
```

## Dependencies

- Raylib

## Author

Carter Kearns (coder.kearns@gmail.com)
