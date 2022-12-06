from datetime import datetime

from .config import Config
from .sleeper import Sleeper

from sleeper_analyzer.exceptions import UninitializedExeception


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
        try:
            return self.sleeper.user_info['username']
        except (TypeError, IndexError, FileNotFoundError, UninitializedExeception):
            return None

    @property
    def last_update(self):
        iso = self.get_config('last_update', '2020-01-01T00:00:00')
        return datetime.fromisoformat(iso)

    @property
    def default_league(self):
        default_league = self.get_config('default_league')
        if default_league is None:
            try:
                default_league = self.sleeper.user_leagues[0]
                default_league = default_league['league_id']
            except (IndexError, FileNotFoundError):
                default_league = None
        return default_league

    @property
    def sleeper(self):
        if self._sleeper is None:
            self._sleeper = Sleeper()
        return self._sleeper

    @property
    def current_week(self):
        try:
            return int(self.sleeper.nfl_state['week'])
        except (IndexError, FileNotFoundError):
            return 0

    @property
    def current_season(self):
        try:
            return int(self.sleeper.nfl_state['season'])
        except (IndexError, FileNotFoundError):
            return 0

    def update(self):
        self.set_config('last_update', datetime.now().isoformat())

    def get_config(self, key, default=None):
        if self.config is None:
            return default
        return self.config.get(key, default)

    def set_config(self, key, value):
        self.config[key] = value
        self.config.save()
