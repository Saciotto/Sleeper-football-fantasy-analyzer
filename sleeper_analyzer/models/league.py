class League(dict):

    def __init__(self, context, name):
        super().__init__()
        self.context = context
        data = self.context.sleeper.get_league(name)
        self.update(data)

    @property
    def id(self):
        return self['league_id']

    @property
    def name(self):
        return self['name']

    @property
    def roster_positions(self):
        return self['roster_positions']

    @property
    def scoring_settings(self):
        return self['scoring_settings']

    @property
    def rosters(self):
        return self.context.sleeper.get_league_rosters(self)

    @property
    def users(self):
        return self.context.sleeper.get_league_users(self)

    def __str__(self):
        return self.name
