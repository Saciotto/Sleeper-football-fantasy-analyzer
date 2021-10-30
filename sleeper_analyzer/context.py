from .config import Config
from .sleeper import Sleeper


class Context:
    _config = None
    _user = None
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

    def get_config(self, key):
        if self.config is None:
            return None
        return self.config.get(key, None)

    def set_config(self, key, value):
        self.config[key] = value
        self.config.save()


