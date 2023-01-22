class Player(dict):

    def __init__(self, db, player_id):
        super().__init__()
        self._db = db
        data = self._db.get_player(player_id)
        self.update(data)
        self._statistics = None
        self._projections = None

    @property
    def id(self):
        return self['player_id']

    @property
    def first_name(self):
        return self.get('first_name', '')

    @property
    def last_name(self):
        return self.get('last_name', 'Unnamed')

    @property
    def name(self):
        return self.get('full_name', f'{self.first_name} {self.last_name}')

    @property
    def age(self):
        return self.get('age', 0)

    @property
    def position(self):
        return self.get('position', '')

    @property
    def fantasy_positions(self):
        return self.get('fantasy_positions', [])

    @property
    def statistics(self):
        if self._statistics is None:
            self._statistics = self._db.get_player_statistics(self.id)
            if self._statistics is None:
                self._statistics = {}
        return self._statistics

    @property
    def projections(self):
        if self._projections is None:
            self._projections = self._db.get_player_projections(self.id)
            if self._projections is None:
                self._projections = {}
        return self._projections

    def current_year_statistics(self, mode='statistics'):
        if mode == 'statistics':
            return self.statistics
        elif mode == 'projections':
            return self.projections
        return None

    def week_statistics(self, week, mode='statistics'):
        stats = self.current_year_statistics(mode)
        week_stats = stats.get(str(week), None)
        if week_stats is None:
            return {}
        return week_stats.get('stats', {})

    def __str__(self):
        return self.name

    __repr__ = __str__
