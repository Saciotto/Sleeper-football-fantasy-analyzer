from datetime import datetime

import sleeper_analyzer.files as files
from sleeper_analyzer.config import Config
from sleeper_analyzer.exceptions import UninitializedExeception
from sleeper_analyzer.sleeper_db import SleeperDatabase
from sleeper_analyzer.models.player import Player
from sleeper_analyzer.models.league import League
from sleeper_analyzer.models.team import Team
from sleeper_analyzer.models.user import User


class Sleeper:

    def __init__(self, path=files.SLEEPER_HOME):
        self.db = SleeperDatabase(path)
        self.config = Config(path)
        self.config.load()

    @property
    def last_download(self):
        iso = self.config.get('last_download', '2020-01-01T00:00:00')
        return datetime.fromisoformat(iso)

    @property
    def default_league(self):
        default_league = self.config.get('default_league', None)
        if default_league is None:
            try:
                default_league = self.db.user_leagues[0]
                default_league = default_league['league_id']
            except (UninitializedExeception):
                default_league = None
        return default_league

    @property
    def default_user(self):
        default_user = self.config.get('default_user', None)
        if default_user is None:
            try:
                default_user = self.db.username
            except (UninitializedExeception):
                default_user = None
        return default_user

    @default_league.setter
    def default_league(self, value):
        self.config['default_league'] = value
        self.config.save()

    @default_user.setter
    def default_user(self, value):
        self.config['default_user'] = value
        self.config.save()

    def download(self, username):
        self.db.download(username)
        self.config['last_download'] = datetime.now().isoformat()
        self.config.save()

    def get_player(self, player_id):
        return Player(self.db, player_id)

    def get_league(self, name):
        return League(self.db, name)

    def get_team(self, user, league):
        return Team(self.db, user, league)

    def get_user(self, user, league=None):
        return User(self.db, user, league)
