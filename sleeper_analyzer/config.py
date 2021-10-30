import json
from pathlib import Path

from . import __version__, DATA_FOLDER


class BaseConfigDict(dict):
    path = Path(f'{DATA_FOLDER}/config.json')

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

    def __init__(self):
        super().__init__()
        self.update(self.DEFAULTS)
