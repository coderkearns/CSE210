import constants


class Director:
    def __init__(self, scenes, video_service, keyboard_service):
        self.all_scenes = {key: Scene(self) for key, Scene in scenes.items()}
        self.current_scene = self.all_scenes[constants.STARTING_SCENE]
        self.current_scene.setup()

        self.video_service = video_service
        self.keyboard_service = keyboard_service

    def start_game(self):
        self.video_service.open_window()
        try:
            while self.video_service.is_window_open():
                next_scene = self.current_scene.run()
                if next_scene is None:
                    break
                self.switch_scene(self.all_scenes[next_scene])
        except KeyboardInterrupt:
            pass
        self.video_service.close_window()

    def switch_scene(self, new_scene):
        self.current_scene = new_scene
        self.current_scene.setup()
