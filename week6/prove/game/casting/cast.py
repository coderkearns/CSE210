class Cast:
    def __init__(self):
        self._actors = {}

    def add_actor(self, group, actor):
        if not group in self._actors.keys():
            self._actors[group] = []
        self._actors[group].append(actor)

    def get_actors(self, group):
        return self._actors.get(group, [])

    def get_all_actors(self):
        return [actor for group in self._actors.values() for actor in group]

    def get_nth_actor(self, group, n):
        group = self._actors.get(group, [])
        if len(group) < n:
            return None
        return group[n]

    def remove_actor(self, group, actor):
        self._actors.get(group, []).remove(actor)
