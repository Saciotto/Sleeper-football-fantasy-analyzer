class User(dict):

    def __init__(self, context, name, league):
        super().__init__()
        self._context = context
        data = self._context.sleeper.get_league_user(name, league)
        self.update(data)

    @property
    def id(self):
        return self['user_id']

    @property
    def name(self):
        return self['display_name']

    def __str__(self):
        return self.name

    __repr__ = __str__
