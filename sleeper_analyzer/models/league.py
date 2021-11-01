from .player import Player


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

    @property
    def players(self):
        for roster in self.rosters:
            for player in roster.get('players', []):
                yield Player(self.context, player)

    def player_score(self, player, week, stats_mode='statistics'):
        week_stats = player.week_statistics(week, stats_mode)
        total = 0
        for k, v in week_stats.items():
            if k in self.scoring_settings:
                total += self.scoring_settings[k] * v
        return total

    def player_scoring_per_week(self, player, stats_mode='statistics', first_week=1, last_week=None):
        if last_week is None:
            last_week = self.context.current_week
        for week in range(first_week, last_week + 1):
            score = self.player_score(player, week, stats_mode)
            yield score

    def _scoring_generator(self, players, stats_mode, first_week, last_week):
        for player in players:
            data = [player.name, player.age, ','.join(player.fantasy_positions)]
            scoring = list(self.player_scoring_per_week(player, stats_mode, first_week, last_week))
            yield data + scoring

    def scoring(self, players, stats_mode='statistics', first_week=1, last_week=None):
        if last_week is None:
            last_week = self.context.current_week
        columns = ['name', 'age', 'position']
        columns += ['week_{}'.format(week) for week in range(first_week, last_week + 1)]
        data = self._scoring_generator(players, stats_mode, first_week, last_week)
        return data, columns

    def __str__(self):
        return self.name

    __repr__ = __str__
