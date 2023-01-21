import json
from pathlib import Path

from . import __version__
from sleeper_analyzer.sleeper import SLEEPER_HOME


class BaseConfigDict(dict):

    def __init__(self, path):
        self.path = Path(path) / 'config.json'

    def ensure_directory(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def exists(self):
        return not self.path.exists()

    def load(self):
        try:
            with self.path.open() as fp:
                data = json.load(fp)
                self.update(data)
        except FileNotFoundError:
            pass

    def save(self):
        self['__meta__'] = {
            'version': __version__
        }
        self.ensure_directory()
        json_string = json.dumps(self, indent=4, sort_keys=True, ensure_ascii=True)
        self.path.write_text(json_string)


class Config(BaseConfigDict):
    DEFAULTS = {
        'default_options': []
    }

    def __init__(self, path=SLEEPER_HOME):
        super().__init__(path)
        self.update(self.DEFAULTS)
