# type: ignore __main__ override
"""
Week 6: Final Project

Author: Carter Kearns
"""
from game.director import Director

from game.services.video_service import VideoService
from game.services.keyboard_service import KeyboardService

from game.scenes.main_scene import MainScene
from game.scenes.play_scene import PlayScene
from game.scenes.game_over_scene import GameOverScene


def main():
    director = Director(
        {"main": MainScene, "play": PlayScene, "game_over": GameOverScene},
        VideoService(),
        KeyboardService(),
    )
    director.start_game()


if __name__ == "__main__":
    main()
