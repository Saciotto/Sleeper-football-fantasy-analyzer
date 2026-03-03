from datetime import datetime

import sleeper_analyzer.files as files
from sleeper_analyzer.config import Config
from sleeper_analyzer.exceptions import UninitializedExeception
from sleeper_analyzer.sleeper_db import SleeperDatabase
from sleeper_analyzer.models.player import Player
from sleeper_analyzer.models.league import League
from sleeper_analyzer.models.team import Team
from sleeper_analyzer.models.user import User


class Sleeper:

    def __init__(self, path=files.SLEEPER_HOME):
        self.db = SleeperDatabase(path)
        self.config = Config(path)
        self.config.load()

    @property
    def last_download(self):
        iso = self.config.get('last_download', '2020-01-01T00:00:00')
        return datetime.fromisoformat(iso)

    @property
    def default_league(self):
        default_league = self.config.get('default_league', None)
        if default_league is None:
            try:
                default_league = self.db.user_leagues[0]
                default_league = default_league['league_id']
            except (UninitializedExeception):
                default_league = None
        return default_league

    @property
    def default_user(self):
        default_user = self.config.get('default_user', None)
        if default_user is None:
            try:
                default_user = self.db.username
            except (UninitializedExeception):
                default_user = None
        return default_user

    @default_league.setter
    def default_league(self, value):
        self.config['default_league'] = value
        self.config.save()

    @default_user.setter
    def default_user(self, value):
        self.config['default_user'] = value
        self.config.save()

    @property
    def followed_users(self):
        return list(self.config.get('followed_users', []))

    def follow(self, username):
        """Add username to the followed list and download their league data."""
        from sleeper_analyzer import downloader
        followed = self.followed_users
        if username not in followed:
            followed.append(username)
            self.config['followed_users'] = followed
            self.config.save()
        downloader.download_followed_user(username, self.db.path)

    def unfollow(self, username):
        """Remove username from the followed list."""
        followed = self.followed_users
        if username in followed:
            followed.remove(username)
            self.config['followed_users'] = followed
            self.config.save()

    def download(self, username):
        self.db.download(username)
        for followed in self.followed_users:
            from sleeper_analyzer import downloader
            downloader.download_followed_user(followed, self.db.path)
        self.config['last_download'] = datetime.now().isoformat()
        self.config.save()

    def get_prospects(self, league, week=None):
        """Find the top 5 prospects per role for the given league.

        Prospects are players present in other downloaded leagues but absent
        from the target league, ranked by projected score.

        Returns a dict mapping role -> list of (Player, score) tuples.
        """
        if isinstance(league, str):
            league = League(self.db, league)
        if week is None:
            week = self.db.current_week

        # Active roster positions, deduplicated (skip bench/IR/TAXI slots)
        bench_slots = {'BN', 'IR', 'TAXI'}
        seen_roles = set()
        unique_roles = []
        for role in league.roster_positions:
            if role not in bench_slots and role not in seen_roles:
                seen_roles.add(role)
                unique_roles.append(role)

        # Player IDs already rostered in the target league
        owned_ids = set()
        for roster in league.rosters:
            owned_ids.update(roster.get('players') or [])

        # Player IDs from every other downloaded league (the prospect pool)
        prospect_ids = set()
        for league_info in self.db.all_leagues:
            if league_info['league_id'] == league.id:
                continue
            for roster in self.db.get_league_rosters(league_info):
                prospect_ids.update(roster.get('players') or [])
        prospect_ids -= owned_ids

        # Positions eligible for each FLEX-type slot
        flex_eligible = {
            'FLEX':       {'RB', 'WR', 'TE'},
            'SUPER_FLEX': {'QB', 'RB', 'WR', 'TE'},
            'IDP_FLEX':   {'LB', 'DB', 'DL'},
        }

        # Score every prospect using the league's scoring settings
        scored = []
        for player_id in prospect_ids:
            try:
                player = Player(self.db, player_id)
                score = league.player_score(player, week, stats_mode='projections')
                if score > 0:
                    scored.append((player, score))
            except Exception:
                continue
        scored.sort(key=lambda x: x[1], reverse=True)

        # Top 5 per role
        results = {}
        for role in unique_roles:
            eligible = flex_eligible.get(role, {role})
            top = [
                (p, s) for p, s in scored
                if set(p.fantasy_positions) & eligible
            ][:5]
            if top:
                results[role] = top
        return results

    def get_player(self, player_id):
        return Player(self.db, player_id)

    def get_league(self, name):
        return League(self.db, name)

    def get_team(self, user, league):
        return Team(self.db, user, league)

    def get_user(self, user, league=None):
        return User(self.db, user, league)
