from datetime import datetime

import sleeper_analyzer.files as files
from sleeper_analyzer.config import Config
from sleeper_analyzer.sleeper_db import SleeperDatabase
from sleeper_analyzer.models.player import Player
from sleeper_analyzer.models.league import League
from sleeper_analyzer.models.team import Team
from sleeper_analyzer.models.user import User


class Sleeper:

    def __init__(self, path=files.SLEEPER_HOME):
        self.db = SleeperDatabase(path)
        self.config = Config(path)

    @property
    def last_download(self):
        iso = self.config.get('last_download', '2020-01-01T00:00:00')
        return datetime.fromisoformat(iso)

    def download(self, username):
        self.db.download(username)
        self.config['last_download'] = datetime.now().isoformat()

    def get_player(self, player_id):
        return Player(self.db, player_id)

    def get_league(self, name):
        return League(self.db, name)

    def get_team(self, user, league):
        return Team(self.db, user, league)

    def get_user(self, user, league=None):
        return User(self.db, user, league)
