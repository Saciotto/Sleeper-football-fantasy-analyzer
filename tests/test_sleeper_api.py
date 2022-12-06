import unittest
from unittest.mock import patch

import tests.mock_requests as requests
from sleeper_analyzer.sleeper_api import SleeperAPI


class TestSleeperAPI(unittest.TestCase):

    @patch('urllib.request.urlopen')
    def test_get_user(self, mock_urlopen):
        mock_urlopen.side_effect = requests.urlopen_by_url
        sleeper = SleeperAPI()
        user = sleeper.get_user('saciotto')
        self.assertEqual(user['username'], 'saciotto')
        self.assertEqual(user['user_id'], '413822753213259776')
        self.assertEqual(user['display_name'], 'Saciotto')

    @patch('urllib.request.urlopen')
    def test_get_all_leagues_for_user(self, mock_urlopen):
        mock_urlopen.side_effect = requests.urlopen_by_url
        sleeper = SleeperAPI()
        leagues = sleeper.get_all_leagues_for_user('413822753213259776', 2022)
        self.assertEqual(len(leagues), 2)
        self.assertEqual(leagues[0]['name'], 'FullGame Dinasty')
        self.assertEqual(leagues[1]['name'], 'SuperFlex Fantasy')

    @patch('urllib.request.urlopen')
    def test_get_league(self, mock_urlopen):
        mock_urlopen.side_effect = requests.urlopen_by_url
        sleeper = SleeperAPI()
        league = sleeper.get_league('784459508880666624')
        self.assertEqual(league['name'], 'SuperFlex Fantasy')

    @patch('urllib.request.urlopen')
    def test_get_rosters(self, mock_urlopen):
        mock_urlopen.side_effect = requests.urlopen_by_url
        sleeper = SleeperAPI()
        rosters = sleeper.get_rosters('784459508880666624')
        self.assertEqual(rosters[0]['players'][0], '4981')

    @patch('urllib.request.urlopen')
    def test_get_users_in_league(self, mock_urlopen):
        mock_urlopen.side_effect = requests.urlopen_by_url
        sleeper = SleeperAPI()
        users = sleeper.get_users_in_league('784459508880666624')
        self.assertEqual(users[0]['user_id'], '303333123121229824')


if __name__ == '__main__':
    unittest.main()
