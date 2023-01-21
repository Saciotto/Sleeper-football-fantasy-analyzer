from pathlib import Path


TEST_FOLDER = Path(__file__).parent
TEMP_FOLDER = TEST_FOLDER / 'temp'
TEST_DATA_FOLDER = TEST_FOLDER / 'data'

CONFIG_FILE = TEST_DATA_FOLDER / 'config.json'
NFL_STATE_FILE = TEST_DATA_FOLDER / 'generic/nfl.json'
PLAYERS_INFO_FILE = TEST_DATA_FOLDER / 'generic/players.json'
USER_INFO_FILE = TEST_DATA_FOLDER / 'user/user.json'
USER_LEAGUES_FILE = TEST_DATA_FOLDER / 'user/leagues.json'
LEAGUE_FOLDER = TEST_DATA_FOLDER / 'generic/leagues'
PLAYER_FOLDER = TEST_DATA_FOLDER / 'generic/players'
