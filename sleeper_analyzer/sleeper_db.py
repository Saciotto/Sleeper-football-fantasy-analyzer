import json
from pathlib import Path

from sleeper_analyzer.exceptions import UserNotFoundException, LeagueNotFoundException, UninitializedExeception
import sleeper_analyzer.files as files
import sleeper_analyzer.utils as utils
import sleeper_analyzer.downloader as downloader


class SleeperDatabase:

    def __init__(self, path=files.SLEEPER_HOME):
        self.path = Path(path)
        self.leagues_path = self.path / files.PATH_LEAGUES_FOLDER
        self.players_path = self.path / files.PATH_PLAYERS_FOLDER
        self._nfl_state = None
        self._players_info = None
        self._user_info = None
        self._user_leagues = None
        self.initialized = False
        self._update_status()

    @property
    def nfl_state(self):
        self._ensure_initialized()
        return self._nfl_state

    @property
    def players_info(self):
        self._ensure_initialized()
        return self._players_info

    @property
    def user_info(self):
        self._ensure_initialized()
        return self._user_info

    @property
    def user_leagues(self):
        self._ensure_initialized()
        return self._user_leagues

    @property
    def users(self):
        self._ensure_initialized()
        added_users = set()
        for league in self.user_leagues:
            for user in self.get_league_users(league):
                user_id = user['user_id']
                if user_id not in added_users:
                    added_users.add(user_id)
                    yield user

    @property
    def current_week(self):
        self._ensure_initialized()
        return int(self.nfl_state['week'])

    @property
    def current_season(self):
        self._ensure_initialized()
        return int(self.nfl_state['season'])

    @property
    def username(self):
        self._ensure_initialized()
        return self.user_info['username']

    def download(self, username):
        downloader.download_statistics(username, self.path)
        self._update_status()

    def get_league(self, name):
        self._ensure_initialized()
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
        self._ensure_initialized()
        if not isinstance(league, dict):
            league = self.get_league(league)
        league_users_path = self.leagues_path / league['league_id'] / 'users.json'
        with league_users_path.open() as fp:
            return json.load(fp)

    def get_league_rosters(self, league):
        self._ensure_initialized()
        if not isinstance(league, dict):
            league = self.get_league(league)
        league_rosters_path = self.leagues_path / league['league_id'] / 'rosters.json'
        with league_rosters_path.open() as fp:
            return json.load(fp)

    def get_league_user(self, name, league):
        self._ensure_initialized()
        users = self.get_league_users(league)
        for user in users:
            if name == user['user_id']:
                return user
            if name.upper() == user['display_name'].upper():
                return user
        raise UserNotFoundException('{} not found in users.json'.format(name))

    def get_player(self, player_id):
        self._ensure_initialized()
        return self.players_info[player_id]

    def get_player_statistics(self, player_id):
        self._ensure_initialized()
        statistics_path = self.players_path / player_id / 'statistics.json'
        with statistics_path.open() as fp:
            return json.load(fp)

    def get_player_projections(self, player_id):
        self._ensure_initialized()
        projections_path = self.players_path / player_id / 'projections.json'
        with projections_path.open() as fp:
            return json.load(fp)

    def _update_status(self):
        nfl_state_file = self.path / files.PATH_NFL_STATE_FILE
        players_file = self.path / files.PATH_PLAYERS_INFO_FILE
        user_info_file = self.path / files.PATH_USER_INFO_FILE
        user_league_file = self.path / files.PATH_USER_LEAGUES_FILE
        try:
            self._nfl_state = utils.load_json_file(nfl_state_file)
            self._players_info = utils.load_json_file(players_file)
            self._user_info = utils.load_json_file(user_info_file)
            self._user_leagues = utils.load_json_file(user_league_file)
            self.initialized = True
        except (FileNotFoundError, IOError):
            self.initialized = False

    def _ensure_initialized(self):
        if not self.initialized:
            raise UninitializedExeception('Folder {} is not initialized'.format(self.path))
