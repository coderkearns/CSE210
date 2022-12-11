class Script:
    def __init__(self, director, cast):
        self._actions = {}

        self._director = director
        self._cast = cast

    def add_action(self, group, action):
        if group not in self._actions.keys():
            self._actions[group] = [action]
        else:
            self._actions[group].append(action)

    def execute(self, group):
        for action in self._actions.get(group, []):
            action.execute(self._director, self._cast, self)
