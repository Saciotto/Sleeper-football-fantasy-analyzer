import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import sleeper_analyzer.utils as utils
from sleeper_analyzer.sleeper_api import SleeperAPI


SLEEPER_HOME = Path.home() / 'Sleeper'

PATH_NFL_STATE_FILE = Path('generic/nfl.json')
PATH_PLAYERS_INFO_FILE = Path('generic/players.json')
PATH_USER_INFO_FILE = Path('user/user.json')
PATH_USER_LEAGUES_FILE = Path('user/leagues.json')

PATH_PLAYERS_FOLDER = Path('generic/players')
PATH_LEAGUES_FOLDER = Path('generic/leagues')


def download_nfl_state(filename):
    filename = Path(filename)
    filename.parent.mkdir(parents=True, exist_ok=True)
    api = SleeperAPI()
    nfl_state = api.get_nfl_state()
    with filename.open('w') as fp:
        json.dump(nfl_state, fp)
    return nfl_state


def download_players_info(filename):
    filename = Path(filename)
    filename.parent.mkdir(parents=True, exist_ok=True)
    api = SleeperAPI()
    players = api.get_all_players()
    with filename.open('w') as fp:
        json.dump(players, fp)
    return players


def download_user_info(filename, username):
    filename = Path(filename)
    filename.parent.mkdir(parents=True, exist_ok=True)
    api = SleeperAPI()
    user = api.get_user(username)
    with filename.open('w') as fp:
        json.dump(user, fp)
    return user


def download_user_leagues(filename, user_id, year):
    filename = Path(filename)
    filename.parent.mkdir(parents=True, exist_ok=True)
    api = SleeperAPI()
    leagues = api.get_all_leagues_for_user(user_id, year)
    with filename.open('w') as fp:
        json.dump(leagues, fp)
    return leagues


def download_league(folder, league_id):
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    api = SleeperAPI()
    league_info = api.get_league(league_id)
    rosters = api.get_rosters(league_id)
    league_users = api.get_users_in_league(league_id)
    league_info_file = folder / 'info.json'
    with league_info_file.open('w') as fp:
        json.dump(league_info, fp)
    rosters_file = folder / 'rosters.json'
    with rosters_file.open('w') as fp:
        json.dump(rosters, fp)
    league_users_file = folder / 'users.json'
    with league_users_file.open('w') as fp:
        json.dump(league_users, fp)
    return league_users, rosters


def download_rosters(folder, player_id, year):
    folder = Path(folder)
    player_folder = folder / player_id
    if not player_folder.exists():
        api = SleeperAPI()
        player_folder.mkdir(parents=True, exist_ok=True)
        player_statistics = api.get_player_statistics(player_id, year)
        player_statistics_file = player_folder / 'statistics.json'
        with player_statistics_file.open('w') as fp:
            json.dump(player_statistics, fp)
        player_projections = api.get_player_projections(player_id, year)
        player_projections_file = player_folder / 'projections.json'
        with player_projections_file.open('w') as fp:
            json.dump(player_projections, fp)


def download_rosters_statistics(user_folder, rosters_folder, users, rosters, year):
    user_folder = Path(user_folder)
    rosters_folder = Path(rosters_folder)
    for user in users:
        user_id = user['user_id']
        user_file = user_folder / user_id / 'user.json'
        players_file = user_folder / user_id / 'players.json'
        user_file.parent.mkdir(parents=True, exist_ok=True)
        with user_file.open('w') as fp:
            json.dump(user, fp)
        for roster in (roster for roster in rosters if roster['owner_id'] == user_id):
            players = roster['players']
            with ThreadPoolExecutor() as executor:
                for player_id in players:
                    executor.submit(download_rosters, rosters_folder, player_id, year)
            with players_file.open('w') as fp:
                json.dump(players, fp)


def download_statistics(username, destination=SLEEPER_HOME):
    destination = Path(destination)

    nfl_file = destination / PATH_NFL_STATE_FILE
    players_file = destination / PATH_PLAYERS_INFO_FILE
    user_info_file = destination / PATH_USER_INFO_FILE
    user_leagues_file = destination / PATH_USER_LEAGUES_FILE
    leagues_folder = destination / PATH_LEAGUES_FOLDER
    players_folder = destination / PATH_PLAYERS_FOLDER

    utils.rm_tree(destination)
    nfl_state = download_nfl_state(nfl_file)
    download_players_info(players_file)
    user = download_user_info(user_info_file, username)

    user_id = user['user_id']
    year = nfl_state['season']

    leagues = download_user_leagues(user_leagues_file, user_id, year)
    for league in leagues:
        league_id = league['league_id']
        folder = leagues_folder / league_id
        users, rosters = download_league(folder, league_id)
        download_rosters_statistics(folder, players_folder, users, rosters, year)
