import unittest
import tests.mock_files as files
from sleeper_analyzer.sleeper import Sleeper

from sleeper_analyzer.exceptions import LeagueNotFoundException, UserNotFoundException
from sleeper_analyzer.utils import load_json_file


class TestSleeper(unittest.TestCase):

    def test_nfl_state(self):
        sleeper = Sleeper(files.TEST_DATA_FOLDER)
        expected = load_json_file(files.NFL_STATE_FILE)
        self.assertEqual(sleeper.nfl_state, expected)

    def test_players_info(self):
        sleeper = Sleeper(files.TEST_DATA_FOLDER)
        expected = load_json_file(files.PLAYERS_INFO_FILE)
        self.assertEqual(sleeper.players_info, expected)

    def test_user_info(self):
        sleeper = Sleeper(files.TEST_DATA_FOLDER)
        expected = load_json_file(files.USER_INFO_FILE)
        self.assertEqual(sleeper.user_info, expected)

    def test_user_leagues(self):
        sleeper = Sleeper(files.TEST_DATA_FOLDER)
        expected = load_json_file(files.USER_LEAGUES_FILE)
        self.assertEqual(sleeper.user_leagues, expected)

    def test_users_list(self):
        sleeper = Sleeper(files.TEST_DATA_FOLDER)
        expected = sleeper.get_league_user('murilocorreia', 'SuperFlex Fantasy')
        users = sleeper.users
        self.assertTrue(expected in users)

    def test_get_league_by_id(self):
        sleeper = Sleeper(files.TEST_DATA_FOLDER)
        expected = load_json_file(files.LEAGUE_FOLDER / '784459508880666624/info.json')
        league = sleeper.get_league('784459508880666624')
        self.assertEqual(league, expected)

    def test_get_league_by_name(self):
        sleeper = Sleeper(files.TEST_DATA_FOLDER)
        expected = load_json_file(files.LEAGUE_FOLDER / '784459508880666624/info.json')
        league = sleeper.get_league('SuperFlex Fantasy')
        self.assertEqual(league, expected)

    def test_get_league_users(self):
        sleeper = Sleeper(files.TEST_DATA_FOLDER)
        expected = load_json_file(files.LEAGUE_FOLDER / '784459508880666624/users.json')
        league = sleeper.get_league('SuperFlex Fantasy')
        user_leagues = sleeper.get_league_users(league)
        self.assertEqual(user_leagues, expected)

    def test_get_league_users_by_name(self):
        sleeper = Sleeper(files.TEST_DATA_FOLDER)
        expected = load_json_file(files.LEAGUE_FOLDER / '784459508880666624/users.json')
        user_leagues = sleeper.get_league_users('SuperFlex Fantasy')
        self.assertEqual(user_leagues, expected)

    def test_get_league_rosters(self):
        sleeper = Sleeper(files.TEST_DATA_FOLDER)
        expected = load_json_file(files.LEAGUE_FOLDER / '784459508880666624/rosters.json')
        league = sleeper.get_league('SuperFlex Fantasy')
        league_rosters = sleeper.get_league_rosters(league)
        self.assertEqual(league_rosters, expected)

    def test_get_league_rosters_by_name(self):
        sleeper = Sleeper(files.TEST_DATA_FOLDER)
        expected = load_json_file(files.LEAGUE_FOLDER / '784459508880666624/rosters.json')
        league_rosters = sleeper.get_league_rosters('SuperFlex Fantasy')
        self.assertEqual(league_rosters, expected)

    def test_get_league_user_by_id(self):
        sleeper = Sleeper(files.TEST_DATA_FOLDER)
        expected = load_json_file(files.LEAGUE_FOLDER / '784459508880666624/303333123121229824/user.json')
        league = sleeper.get_league('SuperFlex Fantasy')
        league_user = sleeper.get_league_user('303333123121229824', league)
        self.assertEqual(league_user, expected)

    def test_get_league_user_by_name(self):
        sleeper = Sleeper(files.TEST_DATA_FOLDER)
        expected = load_json_file(files.LEAGUE_FOLDER / '784459508880666624/303333123121229824/user.json')
        league = sleeper.get_league('SuperFlex Fantasy')
        league_user = sleeper.get_league_user('murilocorreia', league)
        self.assertEqual(league_user, expected)

    def test_get_league_user_by_name_and_league_name(self):
        sleeper = Sleeper(files.TEST_DATA_FOLDER)
        expected = load_json_file(files.LEAGUE_FOLDER / '784459508880666624/303333123121229824/user.json')
        league_user = sleeper.get_league_user('murilocorreia', 'SuperFlex Fantasy')
        self.assertEqual(league_user, expected)

    def test_get_player(self):
        sleeper = Sleeper(files.TEST_DATA_FOLDER)
        expected = load_json_file(files.PLAYERS_INFO_FILE)['167']
        player = sleeper.get_player('167')
        self.assertEqual(player, expected)

    def test_get_player_statistics(self):
        sleeper = Sleeper(files.TEST_DATA_FOLDER)
        expected = load_json_file(files.PLAYER_FOLDER / '167/statistics.json')
        player = sleeper.get_player_statistics('167')
        self.assertEqual(player, expected)

    def test_get_player_projections(self):
        sleeper = Sleeper(files.TEST_DATA_FOLDER)
        expected = load_json_file(files.PLAYER_FOLDER / '167/projections.json')
        player = sleeper.get_player_projections('167')
        self.assertEqual(player, expected)

    def test_league_not_found(self):
        sleeper = Sleeper(files.TEST_DATA_FOLDER)
        with self.assertRaises(LeagueNotFoundException):
            sleeper.get_league('SuperFlex')

    def test_user_not_found(self):
        sleeper = Sleeper(files.TEST_DATA_FOLDER)
        with self.assertRaises(UserNotFoundException):
            sleeper.get_league_user('User', 'SuperFlex Fantasy')
