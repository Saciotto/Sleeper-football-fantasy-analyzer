from types import SimpleNamespace

from pandas import DataFrame

from .league import League
from .player import Player
from .user import User
from ..exceptions import RosterNotFoundException


class Team:

    def __init__(self, context, user, league):
        self._context = context
        if type(league) == str:
            league = League(context, league)
        if type(user) == str:
            user = User(context, user, league)
        self.user = user
        self.league = league

    @property
    def players(self):
        return [Player(self._context, player_id) for player_id in self._get_roster()['players']]

    @property
    def roster_positions(self):
        return self.league.roster_positions

    def scoring_dataframe(self, stats_mode='statistics'):
        data, columns = self.scoring(stats_mode)
        return DataFrame(data, columns=columns)

    def scoring(self, stats_mode='statistics'):
        first_week = 1
        last_week = self._context.current_week
        columns = ['name', 'age', 'position']
        columns += ['week_{}'.format(week) for week in range(first_week, last_week + 1)]
        data = self._scoring_generator(stats_mode, first_week, last_week)
        return data, columns

    def best_projected_lineup(self, week=None):
        if week is None:
            week = self._context.current_week
        starters = self._best_projected_lineup(week)
        lineup = DataFrame(starters)
        lineup = lineup[['name', 'position', 'role', f'week_{week}']]
        lineup = lineup.rename(columns={f'week_{week}': 'projection'})
        return lineup.reset_index(drop=True)

    def player_scoring_per_week(self, player, stats_mode='statistics', first_week=1, last_week=None):
        if last_week is None:
            last_week = self._context.current_week
        return list(self._player_scoring_per_week_generator(player, stats_mode, first_week, last_week))

    def __str__(self):
        return 'Team(User: {}, League: {})'.format(self.user, self.league)

    def _scoring_generator(self, stats_mode, first_week, last_week):
        for player in self.players:
            data = [player.name, player.age, ','.join(player.fantasy_positions)]
            scoring = self.player_scoring_per_week(player, stats_mode, first_week, last_week)
            yield data + scoring

    def _get_roster(self):
        for roster in self.league.rosters:
            if roster['owner_id'] == self.user.id:
                return roster
        raise RosterNotFoundException('Roster for {} not found'.format(self.user.id))

    def _player_scoring_per_week_generator(self, player, stats_mode, first_week, last_week):
        for week in range(first_week, last_week + 1):
            week_stats = player.week_statistics(week, stats_mode)
            item = self._calculate_week_total_points(week_stats)
            yield item

    def _calculate_week_total_points(self, week_stats):
        total = 0
        for k, v in week_stats.items():
            if k in self.league.scoring_settings:
                total += self.league.scoring_settings[k] * v
        return total

    def _best_projected_lineup(self, week):
        projections = self.scoring_dataframe(stats_mode='projections')
        sorted_projections = projections.sort_values(by=f'week_{week}', ascending=False)
        sorted_projections['role'] = ''
        positions = ['RB', 'WR', 'TE', 'QB', 'LB', 'DB', 'DL', 'FLEX', 'SUPER_FLEX', 'IDP_FLEX', 'DEF', 'K']
        roles = {position: self.roster_positions.count(position) for position in positions}
        manager = SimpleNamespace(starters=[], roles=roles, jokers=[])
        for idx, player in sorted_projections.iterrows():
            self._get_available_position(manager, player)
        return manager.starters

    @staticmethod
    def _get_available_position(manager, player):
        positions = player.position.split(',')
        for position in positions:
            if manager.roles.get(position, 0) > 0:
                if len(positions) > 1:
                    joker = {
                        'index': len(manager.starters),
                        'current': position,
                        'destinations': [p for p in positions if p != position]
                    }
                    manager.jokers.append(joker)
                manager.roles[position] -= 1
                player.role = position
                manager.starters.append(player)
                return
        for joker in manager.jokers:
            for position in positions:
                if joker['current'] == position:
                    for destination in joker['destinations']:
                        if manager.roles.get(destination, 0) > 0:
                            manager.starters[joker['index']].role = destination
                            if len(joker['destinations']) > 1:
                                new_joker = {
                                    'index': joker['index'],
                                    'current': destination,
                                    'destinations': [p for p in joker['destinations'] if p != destination]
                                }
                                manager.jokers.append(new_joker)
                            manager.jokers.remove(joker)
                            manager.roles[destination] -= 1
                            player.role = position
                            manager.starters.append(player)
                            return
        flex = ['RB', 'WR', 'TE']
        super_flex = ['RB', 'WR', 'TE', 'QB']
        idp_flex = ['LB', 'DB', 'DL']
        for position in positions:
            if manager.roles.get('FLEX', 0) > 0 and position in flex:
                manager.roles['FLEX'] -= 1
                player.role = 'FLEX'
                manager.starters.append(player)
                return
            if manager.roles.get('SUPER_FLEX', 0) > 0 and position in super_flex:
                manager.roles['SUPER_FLEX'] -= 1
                player.role = 'SUPER_FLEX'
                manager.starters.append(player)
                return
            if manager.roles.get('IDP_FLEX', 0) > 0 and position in idp_flex:
                manager.roles['IDP_FLEX'] -= 1
                player.role = 'IDP_FLEX'
                manager.starters.append(player)
                return
