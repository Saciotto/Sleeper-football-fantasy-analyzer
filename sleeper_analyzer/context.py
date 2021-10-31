from .config import Config
from .sleeper import Sleeper


class Context:
    _config = None
    _sleeper = None

    @property
    def config(self):
        if self._config is None:
            self._config = Config()
            self._config.load()
        return self._config

    @property
    def username(self):
        return self.get_config('username')

    @property
    def default_league(self):
        default_league = self.get_config('default_league')
        if default_league is None:
            try:
                default_league = self.sleeper.user_leagues[0]
                default_league = default_league['league_id']
            except IndexError:
                default_league = None
        return default_league

    @property
    def sleeper(self):
        if self._sleeper is None:
            self._sleeper = Sleeper()
        return self._sleeper

    @property
    def current_week(self):
        return int(self.sleeper.nfl_state['week'])

    @property
    def current_season(self):
        return int(self.sleeper.nfl_state['season'])

    @username.setter
    def username(self, name):
        self.set_config('username', name)

    def get_config(self, key, default=None):
        if self.config is None:
            return default
        return self.config.get(key, default)

    def set_config(self, key, value):
        self.config[key] = value
        self.config.save()


