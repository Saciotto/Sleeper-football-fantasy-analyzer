import json

from PySide6.QtCore import QObject, Signal, Property, Slot


class TeamController(QObject):
    selectedLeagueChanged = Signal()
    selectedUserChanged = Signal()
    playersChanged = Signal()

    def __init__(self, parent):
        QObject.__init__(self, parent)
        self._sleeper = parent.sleeper
        self.selectedLeagueChanged.connect(self.playersChanged)
        self.selectedUserChanged.connect(self.playersChanged)

    @Property(list, constant=True)
    def leagues(self):
        return [league['name'] for league in self.sleeper.db.user_leagues]

    @Property(list, notify=selectedLeagueChanged)
    def leagueUsers(self):
        return self._league_users

    @Property(str, notify=selectedLeagueChanged)
    def selectedLeague(self):
        return self._selected_league

    @Property(str, notify=selectedUserChanged)
    def selectedUser(self):
        return self._selected_user

    @Property(str, notify=playersChanged)
    def players(self):
        positions_order = ['QB', 'RB', "WR", 'TE', 'DL', 'LB', 'DB', 'LAST']
        order = {key: i for i, key in enumerate(positions_order)}
        team = self._sleeper.get_team(self._selected_user, self._selected_league)
        players = team.players
        players.sort(key=lambda p: (order.get(p.fantasy_positions[0], order['LAST']), p.fantasy_positions[0], p.name))
        return json.dumps(players)

    @selectedUser.setter
    def selectedUser(self, username):
        if self._selected_user != username:
            self._selected_user = username
            self.selectedUserChanged.emit()

    @selectedLeague.setter
    def selectedLeague(self, league_name):
        if self._selected_league != league_name:
            self._selected_league = league_name
            league = self._sleeper.get_league(self._selected_league)
            self._league_users = [user['display_name'] for user in league.users]
            if self._selected_user not in self._league_users:
                self.selectedUser = self._league_users[0]
            self.selectedLeagueChanged.emit()

    @Slot(str, result=str)
    def playerStatistics(self, player_id):
        player = self._sleeper.get_player(player_id)
        return json.dumps(player.statistics)

    @Slot()
    def update(self):
        league_name = self._sleeper.default_league
        selected_league = self._sleeper.get_league(league_name)
        self._selected_league = selected_league.name
        self._league_users = [user['display_name'] for user in selected_league.users]
        self._selected_user = self._sleeper.db.username
