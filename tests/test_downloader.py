import filecmp
import json
import unittest
from unittest.mock import patch
from urllib.request import HTTPError

import tests.mock_requests as requests
import tests.mock_files as files
from sleeper_analyzer.utils import rm_tree
from sleeper_analyzer import downloader


class TestDownloader(unittest.TestCase):

    def setUp(self):
        rm_tree(files.TEMP_FOLDER)

    def tearDown(self):
        rm_tree(files.TEMP_FOLDER)

    @patch('urllib.request.urlopen')
    def test_download_nfl_state(self, mock_urlopen):
        mock_urlopen.side_effect = requests.urlopen_by_url
        filename = files.TEMP_FOLDER / 'nfl.json'
        downloader.download_nfl_state(filename)
        self.assertTrue(filecmp.cmp(filename, files.NFL_STATE_FILE, shallow=False))

    @patch('urllib.request.urlopen')
    def test_download_players_info(self, mock_urlopen):
        mock_urlopen.side_effect = requests.urlopen_by_url
        filename = files.TEMP_FOLDER / 'players.json'
        downloader.download_players_info(filename)
        self.assertTrue(filecmp.cmp(filename, files.PLAYERS_INFO_FILE, shallow=False))

    @patch('urllib.request.urlopen')
    def test_download_user_info(self, mock_urlopen):
        mock_urlopen.side_effect = requests.urlopen_by_url
        filename = files.TEMP_FOLDER / 'user.json'
        downloader.download_user_info(filename, 'username')
        self.assertTrue(filecmp.cmp(filename, files.USER_INFO_FILE, shallow=False))

    @patch('urllib.request.urlopen')
    def test_download_user_leagues(self, mock_urlopen):
        mock_urlopen.side_effect = requests.urlopen_by_url
        filename = files.TEMP_FOLDER / 'leagues.json'
        downloader.download_user_leagues(filename, '413822753213259776', 2022)
        self.assertTrue(filecmp.cmp(filename, files.USER_LEAGUES_FILE, shallow=False))

    @patch('urllib.request.urlopen')
    def test_download_league(self, mock_urlopen):
        league_id = '784459508880666624'
        mock_urlopen.side_effect = requests.urlopen_by_url
        folder = files.TEMP_FOLDER
        league_info_file = folder / 'info.json'
        rosters_file = folder / 'rosters.json'
        league_users_file = folder / 'users.json'
        league_info_orig = files.LEAGUE_FOLDER / league_id / 'info.json'
        rosters_orig = files.LEAGUE_FOLDER / league_id / 'rosters.json'
        league_users_orig = files.LEAGUE_FOLDER / league_id / 'users.json'
        downloader.download_league(folder, league_id)
        self.assertTrue(filecmp.cmp(league_info_file, league_info_orig, shallow=False))
        self.assertTrue(filecmp.cmp(rosters_file, rosters_orig, shallow=False))
        self.assertTrue(filecmp.cmp(league_users_file, league_users_orig, shallow=False))

    @patch('urllib.request.urlopen')
    def test_download_rosters(self, mock_urlopen):
        player_id = '6853'
        mock_urlopen.side_effect = requests.urlopen_by_url
        folder = files.TEMP_FOLDER
        statistics_file = folder / player_id / 'statistics.json'
        projections_file = folder / player_id / 'projections.json'
        statistics_orig = files.PLAYER_FOLDER / player_id / 'statistics.json'
        projections_orig = files.PLAYER_FOLDER / player_id / 'projections.json'
        downloader.download_rosters(folder, player_id, 2022)
        self.assertTrue(filecmp.cmp(statistics_file, statistics_orig, shallow=False))
        self.assertTrue(filecmp.cmp(projections_file, projections_orig, shallow=False))

    @patch('urllib.request.urlopen')
    def test_download_rosters_statistics(self, mock_urlopen):
        league_id = '784459508880666624'
        player_id = '413822753213259776'
        mock_urlopen.side_effect = requests.urlopen_by_url
        user_folder = files.TEMP_FOLDER / 'user'
        rosters_folder = files.TEMP_FOLDER / 'players'
        user_file = user_folder / player_id / 'user.json'
        players_file = user_folder / player_id / 'players.json'
        user_orig = files.LEAGUE_FOLDER / league_id / player_id / 'user.json'
        players_orig = files.LEAGUE_FOLDER / league_id / player_id / 'players.json'
        users = [json.loads(user_orig.read_text())]
        rosters = json.loads((files.LEAGUE_FOLDER / league_id / 'rosters.json').read_text())
        downloader.download_rosters_statistics(user_folder, rosters_folder, users, rosters, 2022)
        self.assertTrue(filecmp.cmp(user_file, user_orig, shallow=False))
        self.assertTrue(filecmp.cmp(players_file, players_orig, shallow=False))

    @patch('urllib.request.urlopen')
    def test_download_statistics(self, mock_urlopen):
        mock_urlopen.side_effect = requests.urlopen_by_url
        nfl_file = files.TEMP_FOLDER / 'generic/nfl.json'
        nfl_orig = files.NFL_STATE_FILE
        players_info_file = files.TEMP_FOLDER / 'generic/players.json'
        players_info_orig = files.PLAYERS_INFO_FILE
        user_info_file = files.TEMP_FOLDER / 'user/user.json'
        user_info_orig = files.USER_INFO_FILE
        user_leagues_file = files.TEMP_FOLDER / 'user/leagues.json'
        user_leagues_orig = files.USER_LEAGUES_FILE
        downloader.download_statistics('username', files.TEMP_FOLDER)
        self.assertTrue(filecmp.cmp(nfl_file, nfl_orig, shallow=False))
        self.assertTrue(filecmp.cmp(players_info_file, players_info_orig, shallow=False))
        self.assertTrue(filecmp.cmp(user_info_file, user_info_orig, shallow=False))
        self.assertTrue(filecmp.cmp(user_leagues_file, user_leagues_orig, shallow=False))

    @patch('urllib.request.urlopen')
    def test_download_statistics_no_response(self, mock_urlopen):
        mock_urlopen.side_effect = TimeoutError("Timeout error")
        with self.assertRaises(TimeoutError):
            downloader.download_statistics('username', files.TEMP_FOLDER)

    @patch('urllib.request.urlopen')
    def test_download_statistics_server_error(self, mock_urlopen):
        mock_urlopen.side_effect = HTTPError('http://example.com', 500, 'Internal Error', {}, None)
        with self.assertRaises(HTTPError):
            downloader.download_statistics('username', files.TEMP_FOLDER)


if __name__ == '__main__':
    unittest.main()
