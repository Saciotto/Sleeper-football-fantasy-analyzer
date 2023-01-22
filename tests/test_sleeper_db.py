import unittest
from unittest.mock import patch
from sleeper_analyzer.sleeper_db import SleeperDatabase

import tests.mock_requests as requests
import tests.mock_files as files
import sleeper_analyzer.utils as utils
from sleeper_analyzer.exceptions import LeagueNotFoundException, UserNotFoundException, UninitializedExeception


class TestSleeperDatabase(unittest.TestCase):

    def test_nfl_state(self):
        sleeper = SleeperDatabase(files.TEST_DATA_FOLDER)
        expected = utils.load_json_file(files.NFL_STATE_FILE)
        self.assertEqual(sleeper.nfl_state, expected)

    def test_players_info(self):
        sleeper = SleeperDatabase(files.TEST_DATA_FOLDER)
        expected = utils.load_json_file(files.PLAYERS_INFO_FILE)
        self.assertEqual(sleeper.players_info, expected)

    def test_user_info(self):
        sleeper = SleeperDatabase(files.TEST_DATA_FOLDER)
        expected = utils.load_json_file(files.USER_INFO_FILE)
        self.assertEqual(sleeper.user_info, expected)

    def test_user_leagues(self):
        sleeper = SleeperDatabase(files.TEST_DATA_FOLDER)
        expected = utils.load_json_file(files.USER_LEAGUES_FILE)
        self.assertEqual(sleeper.user_leagues, expected)

    def test_users_list(self):
        sleeper = SleeperDatabase(files.TEST_DATA_FOLDER)
        expected = sleeper.get_league_user('murilocorreia', 'SuperFlex Fantasy')
        users = sleeper.users
        self.assertTrue(expected in users)

    def test_get_league_by_id(self):
        sleeper = SleeperDatabase(files.TEST_DATA_FOLDER)
        expected = utils.load_json_file(files.LEAGUE_FOLDER / '784459508880666624/info.json')
        league = sleeper.get_league('784459508880666624')
        self.assertEqual(league, expected)

    def test_get_league_by_name(self):
        sleeper = SleeperDatabase(files.TEST_DATA_FOLDER)
        expected = utils.load_json_file(files.LEAGUE_FOLDER / '784459508880666624/info.json')
        league = sleeper.get_league('SuperFlex Fantasy')
        self.assertEqual(league, expected)

    def test_get_league_users(self):
        sleeper = SleeperDatabase(files.TEST_DATA_FOLDER)
        expected = utils.load_json_file(files.LEAGUE_FOLDER / '784459508880666624/users.json')
        league = sleeper.get_league('SuperFlex Fantasy')
        user_leagues = sleeper.get_league_users(league)
        self.assertEqual(user_leagues, expected)

    def test_get_league_users_by_name(self):
        sleeper = SleeperDatabase(files.TEST_DATA_FOLDER)
        expected = utils.load_json_file(files.LEAGUE_FOLDER / '784459508880666624/users.json')
        user_leagues = sleeper.get_league_users('SuperFlex Fantasy')
        self.assertEqual(user_leagues, expected)

    def test_get_league_rosters(self):
        sleeper = SleeperDatabase(files.TEST_DATA_FOLDER)
        expected = utils.load_json_file(files.LEAGUE_FOLDER / '784459508880666624/rosters.json')
        league = sleeper.get_league('SuperFlex Fantasy')
        league_rosters = sleeper.get_league_rosters(league)
        self.assertEqual(league_rosters, expected)

    def test_get_league_rosters_by_name(self):
        sleeper = SleeperDatabase(files.TEST_DATA_FOLDER)
        expected = utils.load_json_file(files.LEAGUE_FOLDER / '784459508880666624/rosters.json')
        league_rosters = sleeper.get_league_rosters('SuperFlex Fantasy')
        self.assertEqual(league_rosters, expected)

    def test_get_league_user_by_id(self):
        sleeper = SleeperDatabase(files.TEST_DATA_FOLDER)
        expected = utils.load_json_file(files.LEAGUE_FOLDER / '784459508880666624/303333123121229824/user.json')
        league = sleeper.get_league('SuperFlex Fantasy')
        league_user = sleeper.get_league_user('303333123121229824', league)
        self.assertEqual(league_user, expected)

    def test_get_league_user_by_name(self):
        sleeper = SleeperDatabase(files.TEST_DATA_FOLDER)
        expected = utils.load_json_file(files.LEAGUE_FOLDER / '784459508880666624/303333123121229824/user.json')
        league = sleeper.get_league('SuperFlex Fantasy')
        league_user = sleeper.get_league_user('murilocorreia', league)
        self.assertEqual(league_user, expected)

    def test_get_league_user_by_name_and_league_name(self):
        sleeper = SleeperDatabase(files.TEST_DATA_FOLDER)
        expected = utils.load_json_file(files.LEAGUE_FOLDER / '784459508880666624/303333123121229824/user.json')
        league_user = sleeper.get_league_user('murilocorreia', 'SuperFlex Fantasy')
        self.assertEqual(league_user, expected)

    def test_get_player(self):
        sleeper = SleeperDatabase(files.TEST_DATA_FOLDER)
        expected = utils.load_json_file(files.PLAYERS_INFO_FILE)['167']
        player = sleeper.get_player('167')
        self.assertEqual(player, expected)

    def test_get_player_statistics(self):
        sleeper = SleeperDatabase(files.TEST_DATA_FOLDER)
        expected = utils.load_json_file(files.PLAYER_FOLDER / '167/statistics.json')
        player = sleeper.get_player_statistics('167')
        self.assertEqual(player, expected)

    def test_get_player_projections(self):
        sleeper = SleeperDatabase(files.TEST_DATA_FOLDER)
        expected = utils.load_json_file(files.PLAYER_FOLDER / '167/projections.json')
        player = sleeper.get_player_projections('167')
        self.assertEqual(player, expected)

    def test_league_not_found(self):
        sleeper = SleeperDatabase(files.TEST_DATA_FOLDER)
        with self.assertRaises(LeagueNotFoundException):
            sleeper.get_league('SuperFlex')

    def test_user_not_found(self):
        sleeper = SleeperDatabase(files.TEST_DATA_FOLDER)
        with self.assertRaises(UserNotFoundException):
            sleeper.get_league_user('User', 'SuperFlex Fantasy')

    def test_unitialized(self):
        sleeper = SleeperDatabase(files.TEMP_FOLDER)
        with self.assertRaises(UninitializedExeception):
            sleeper.get_league_user('User', 'SuperFlex Fantasy')


class TestSleeperDatabaseDownloader(unittest.TestCase):

    def setUp(self):
        utils.rm_tree(files.TEMP_FOLDER)

    def tearDown(self):
        utils.rm_tree(files.TEMP_FOLDER)

    @patch('urllib.request.urlopen')
    def test_download(self, mock_urlopen):
        mock_urlopen.side_effect = requests.urlopen_by_url
        sleeper = SleeperDatabase(files.TEMP_FOLDER)
        sleeper.download('username')
        expected = utils.load_json_file(files.NFL_STATE_FILE)
        self.assertEqual(sleeper.nfl_state, expected)
