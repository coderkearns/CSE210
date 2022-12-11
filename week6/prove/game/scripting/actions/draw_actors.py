from ..action import Action


class DrawActorsAction(Action):
    def execute(self, director, cast, script):
        director.video_service.clear_buffer()
        director.video_service.draw_actors(cast.get_all_actors())
        director.video_service.flush_buffer()
