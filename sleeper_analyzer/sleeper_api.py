import json
import urllib.request


class SleeperAPI:
    def __init__(self, timeout=5):
        self._timeout = timeout

    def _get(self, url):
        request = urllib.request.Request(url, method='GET')
        with urllib.request.urlopen(request, timeout=self._timeout) as response:
            return json.load(response)

    def get_user(self, user_name):
        url = 'https://api.sleeper.app/v1/user/{}'.format(user_name)
        return self._get(url)

    def get_all_leagues_for_user(self, user_id, season):
        url = 'https://api.sleeper.app/v1/user/{}/leagues/nfl/{}'.format(user_id, season)
        return self._get(url)

    def get_league(self, league_id):
        url = 'https://api.sleeper.app/v1/league/{}'.format(league_id)
        return self._get(url)

    def get_rosters(self, league_id):
        url = 'https://api.sleeper.app/v1/league/{}/rosters'.format(league_id)
        return self._get(url)

    def get_users_in_league(self, league_id):
        url = 'https://api.sleeper.app/v1/league/{}/users'.format(league_id)
        return self._get(url)

    def get_league_matchups(self, league_id, week):
        url = 'https://api.sleeper.app/v1/league/{}/matchups/{}'.format(league_id, week)
        return self._get(url)

    def get_playoffs_winners_brackets(self, league_id):
        url = 'https://api.sleeper.app/v1/league/{}/winners_bracket'.format(league_id)
        return self._get(url)

    def get_playoffs_losers_brackets(self, league_id):
        url = 'https://api.sleeper.app/v1/league/{}/loses_bracket'.format(league_id)
        return self._get(url)

    def get_transactions(self, league_id, week):
        url = 'https://api.sleeper.app/v1/league/{}/transactions/{}'.format(league_id, week)
        return self._get(url)

    def get_traded_picks(self, league_id):
        url = 'https://api.sleeper.app/v1/league/{}/traded_picks'.format(league_id)
        return self._get(url)

    def get_nfl_state(self):
        url = 'https://api.sleeper.app/v1/state/nfl'
        return self._get(url)

    def get_drafts_for_user(self, user_id, season):
        url = 'https://api.sleeper.app/v1/user/{}/drafts/nfl/{}'.format(user_id, season)
        return self._get(url)

    def get_drafts_for_league(self, league_id):
        url = 'https://api.sleeper.app/v1/league/{}/drafts'.format(league_id)
        return self._get(url)

    def get_draft(self, draft_id):
        url = 'https://api.sleeper.app/v1/draft/{}'.format(draft_id)
        return self._get(url)

    def get_draft_picks(self, draft_id):
        url = 'https://api.sleeper.app/v1/draft/{}/picks'.format(draft_id)
        return self._get(url)

    def get_draft_traded_picks(self, draft_id):
        url = 'https://api.sleeper.app/v1/draft/{}/traded_picks'.format(draft_id)
        return self._get(url)

    def get_all_players(self):
        url = 'https://api.sleeper.app/v1/players/nfl'
        return self._get(url)

    def get_add_trending_players(self, lookback_hours=24, limit=25):
        url = 'https://api.sleeper.app/v1/players/nfl/trending/add?lookback_hours={}&limit={}' \
            .format(lookback_hours, limit)
        return self._get(url)

    def get_drop_trending_players(self, lookback_hours=24, limit=25):
        url = 'https://api.sleeper.app/v1/players/nfl/trending/drop?lookback_hours={}&limit={}' \
            .format(lookback_hours, limit)
        return self._get(url)

    def get_player_projections(self, player_id, season):
        url = 'https://api.sleeper.app/projections/nfl/player/{}?season_type=regular&season={}&grouping=week' \
            .format(player_id, season)
        return self._get(url)

    def get_player_statistics(self, player_id, season):
        url = 'https://api.sleeper.app/stats/nfl/player/{}?season_type=regular&season={}&grouping=week' \
            .format(player_id, season)
        return self._get(url)
