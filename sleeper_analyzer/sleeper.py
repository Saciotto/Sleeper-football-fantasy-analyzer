import json
from pathlib import Path

from .exceptions import UserNotFoundException, LeagueNotFoundException
from .utils import load_json_file

SLEEPER_HOME = Path.home() / 'Sleeper'


class Sleeper:

    def __init__(self, path=SLEEPER_HOME):
        self.path = Path(path)
        nfl_state_file = self.path / 'generic/nfl.json'
        players_file = self.path / 'generic/players.json'
        user_info_file = self.path / 'user/user.json'
        user_league_file = self.path / 'user/leagues.json'
        self.leagues_path = self.path / 'generic/leagues'
        self.players_path = self.path / 'generic/players'
        self.nfl_state = load_json_file(nfl_state_file)
        self.players_info = load_json_file(players_file)
        self.user_info = load_json_file(user_info_file)
        self.user_leagues = load_json_file(user_league_file)

    @property
    def users(self):
        added_users = set()
        for league in self.user_leagues:
            for user in self.get_league_users(league):
                user_id = user['user_id']
                if user_id not in added_users:
                    added_users.add(user_id)
                    yield user

    def get_league(self, name):
        for league_path in self.leagues_path.iterdir():
            league_info_path = league_path / 'info.json'
            with league_info_path.open() as fp:
                league = json.load(fp)
            if name == league['league_id']:
                return league
            elif name.upper() == league['name'].upper():
                return league
        raise LeagueNotFoundException('{} not found in user_leagues.json'.format(name))

    def get_league_users(self, league):
        if not isinstance(league, dict):
            league = self.get_league(league)
        league_users_path = self.leagues_path / league['league_id'] / 'users.json'
        with league_users_path.open() as fp:
            return json.load(fp)

    def get_league_rosters(self, league):
        if not isinstance(league, dict):
            league = self.get_league(league)
        league_rosters_path = self.leagues_path / league['league_id'] / 'rosters.json'
        with league_rosters_path.open() as fp:
            return json.load(fp)

    def get_league_user(self, name, league):
        users = self.get_league_users(league)
        for user in users:
            if name == user['user_id']:
                return user
            if name.upper() == user['display_name'].upper():
                return user
        raise UserNotFoundException('{} not found in users.json'.format(name))

    def get_player(self, player_id):
        return self.players_info[player_id]

    def get_player_statistics(self, player_id):
        statistics_path = self.players_path / player_id / 'statistics.json'
        with statistics_path.open() as fp:
            return json.load(fp)

    def get_player_projections(self, player_id):
        projections_path = self.players_path / player_id / 'projections.json'
        with projections_path.open() as fp:
            return json.load(fp)
