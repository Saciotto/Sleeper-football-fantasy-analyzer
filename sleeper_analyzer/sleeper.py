import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from . import DATA_FOLDER
from .exceptions import UserNotFoundException, LeagueNotFoundException
from .sleeper_api import SleeperAPI


class Sleeper:
    sleeper_path = Path(f'{DATA_FOLDER}/sleeper')
    nfl_state_path = sleeper_path / 'nfl.json'
    players_info_path = sleeper_path / 'players.json'
    user_info_path = sleeper_path / 'user.json'
    user_leagues_path = sleeper_path / 'user_leagues.json'
    leagues_path = sleeper_path / 'leagues'
    players_path = sleeper_path / 'players'

    _nfl_state = None
    _players_info = None
    _user_info = None
    _user_leagues = None

    @property
    def nfl_state(self):
        if self._nfl_state is None:
            with self.nfl_state_path.open() as fp:
                self._nfl_state = json.load(fp)
        return self._nfl_state

    @property
    def players_info(self):
        if self._players_info is None:
            with self.players_info_path.open() as fp:
                self._players_info = json.load(fp)
        return self._players_info

    @property
    def user_info(self):
        if self._user_info is None:
            with self.user_info_path.open() as fp:
                self._user_info = json.load(fp)
        return self._user_info

    @property
    def user_leagues(self):
        if self._user_leagues is None:
            with self.user_leagues_path.open() as fp:
                self._user_leagues = json.load(fp)
        return self._user_leagues

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
            league_info_path = league_path / 'league_info.json'
            with league_info_path.open() as fp:
                league = json.load(fp)
            if name == league['league_id']:
                return league
            elif name.upper() == league['name'].upper():
                return league
        raise LeagueNotFoundException('{} not found in user_leagues.json'.format(name))

    def get_league_users(self, league):
        league_users_path = self.leagues_path / league['league_id'] / 'users.json'
        with league_users_path.open() as fp:
            return json.load(fp)

    def get_league_rosters(self, league):
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

    def download_statistics(self, username, year=None):
        self._clear_data_folder()
        nfl_state = self._download_nfl_state()
        self._download_players_info()
        if year is None:
            year = nfl_state['season']
        user, leagues = self._download_user_leagues(username, year)
        for league in leagues:
            league_id = league['league_id']
            users, rosters = self._download_leagues(league_id)
            self._download_players_statistics(league_id, users, rosters)

    def _rm_tree(self, folder):
        for child in folder.glob('*'):
            if child.is_file():
                child.unlink()
            else:
                self._rm_tree(child)
        folder.rmdir()

    def _clear_data_folder(self):
        if self.sleeper_path.exists():
            self._rm_tree(self.sleeper_path)

    def _download_nfl_state(self):
        self.nfl_state_path.parent.mkdir(parents=True, exist_ok=True)
        api = SleeperAPI()
        state = api.get_nfl_state()
        with self.nfl_state_path.open('w') as fp:
            json.dump(state, fp)
        self._nfl_state = state
        return state

    def _download_players_info(self):
        self.players_info_path.parent.mkdir(parents=True, exist_ok=True)
        api = SleeperAPI()
        players = api.get_all_players()
        with self.players_info_path.open('w') as fp:
            json.dump(players, fp)
        self._players_info = players

    def _download_user_leagues(self, username, year):
        api = SleeperAPI()
        self.user_info_path.parent.mkdir(parents=True, exist_ok=True)
        user = api.get_user(username)
        with self.user_info_path.open('w') as fp:
            json.dump(user, fp)
        self._user_info = user
        user_id = user['user_id']
        self.user_leagues_path.parent.mkdir(parents=True, exist_ok=True)
        leagues = api.get_all_leagues_for_user(user_id, year)
        with self.user_leagues_path.open('w') as fp:
            json.dump(leagues, fp)
        self._user_leagues = leagues
        return user, leagues

    def _download_leagues(self, league_id):
        api = SleeperAPI()
        league_path = self.leagues_path / league_id
        league_path.mkdir(parents=True, exist_ok=True)
        league_info = api.get_league(league_id)
        rosters = api.get_rosters(league_id)
        league_users = api.get_users_in_league(league_id)
        league_info_path = league_path / 'league_info.json'
        with league_info_path.open('w') as fp:
            json.dump(league_info, fp)
        rosters_path = league_path / 'rosters.json'
        with rosters_path.open('w') as fp:
            json.dump(rosters, fp)
        league_users_path = league_path / 'users.json'
        with league_users_path.open('w') as fp:
            json.dump(league_users, fp)
        return league_users, rosters

    def _download_rosters(self, player_id):
        player_folder = self.players_path / player_id
        if not player_folder.exists():
            api = SleeperAPI()
            player_folder.mkdir(parents=True, exist_ok=True)
            player_statistics = api.get_player_statistics(player_id)
            player_statistics_path = player_folder / 'statistics.json'
            with player_statistics_path.open('w') as fp:
                json.dump(player_statistics, fp)
            player_projections = api.get_player_projections(player_id)
            player_projections_path = player_folder / 'projections.json'
            with player_projections_path.open('w') as fp:
                json.dump(player_projections, fp)

    def _download_players_statistics(self, league_id, users, rosters):
        league_path = self.leagues_path / league_id
        for user in users:
            user_id = user['user_id']
            user_path = league_path / user_id / 'user.json'
            user_players_path = league_path / user_id / 'players.json'
            user_path.parent.mkdir(parents=True, exist_ok=True)
            with user_path.open('w') as fp:
                json.dump(user, fp)
            for roster in (roster for roster in rosters if roster['owner_id'] == user_id):
                players = roster['players']
                with ThreadPoolExecutor() as executor:
                    for player_id in players:
                        executor.submit(self._download_rosters, player_id)
                with user_players_path.open('w') as fp:
                    json.dump(players, fp)
