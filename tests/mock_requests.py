import re
from unittest.mock import MagicMock

import tests.mock_files as files


def urlopen_by_url(url, data=None, timeout=30, *, cafile=None, capath=None, cadefault=False, context=None):
    cm = MagicMock()
    cm.getcode.return_value = 200
    cm.__enter__.return_value = cm
    re_nfl_state = re.compile(r'https://api.sleeper.app/v1/state/nfl$')
    re_players_info = re.compile(r'https://api.sleeper.app/v1/players/nfl$')
    re_user_info = re.compile(r'https://api.sleeper.app/v1/user/\w+$')
    re_user_leagues = re.compile(r'https://api.sleeper.app/v1/user/(\d+)/leagues/nfl/(\d+)$')
    re_get_league = re.compile(r'https://api.sleeper.app/v1/league/(\d+)$')
    re_rosters = re.compile(r'https://api.sleeper.app/v1/league/(\d+)/rosters$')
    re_league_users = re.compile(r'https://api.sleeper.app/v1/league/(\d+)/users$')
    re_player_statistics = re.compile(
        r'https://api.sleeper.app/stats/nfl/player/(\d+)\?season_type=regular&season=(\d+)&grouping=week$')
    re_player_projections = re.compile(
        r'https://api.sleeper.app/projections/nfl/player/(\d+)\?season_type=regular&season=(\d+)&grouping=week$')
    if re_nfl_state.match(url.full_url):
        cm.read.return_value = files.NFL_STATE_FILE.read_text()
    elif re_players_info.match(url.full_url):
        cm.read.return_value = files.PLAYERS_INFO_FILE.read_text()
    elif re_user_info.match(url.full_url):
        cm.read.return_value = files.USER_INFO_FILE.read_text()
    elif re_user_leagues.match(url.full_url):
        cm.read.return_value = files.USER_LEAGUES_FILE.read_text()
    elif m := re_get_league.match(url.full_url):
        filename = files.LEAGUE_FOLDER / m.group(1) / 'info.json'
        cm.read.return_value = filename.read_text()
    elif m := re_rosters.match(url.full_url):
        filename = files.LEAGUE_FOLDER / m.group(1) / 'rosters.json'
        cm.read.return_value = filename.read_text()
    elif m := re_league_users.match(url.full_url):
        filename = files.LEAGUE_FOLDER / m.group(1) / 'users.json'
        cm.read.return_value = filename.read_text()
    elif m := re_player_statistics.match(url.full_url):
        filename = files.PLAYER_FOLDER / m.group(1) / 'statistics.json'
        cm.read.return_value = filename.read_text()
    elif m := re_player_projections.match(url.full_url):
        filename = files.PLAYER_FOLDER / m.group(1) / 'projections.json'
        cm.read.return_value = filename.read_text()
    return cm
