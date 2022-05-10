import json
from PySide6.QtCore import QObject, Signal, Property
from sleeper_analyzer.models.team import Team
from sleeper_analyzer.models.league import League


class TeamController(QObject):
    leagueChanged = Signal()
    usersChanged = Signal()
    usernameChanged = Signal()
    playersChanged = Signal()

    def __init__(self, parent, username=None, league=None):
        QObject.__init__(self, parent)
        self._master = parent
        if username is None:
            self._username = self._master.context.username
        else:
            self._username = username
        if league is None:
            league = self._master.context.default_league
        self._league = League(self._master.context, league).name

        self.leagueChanged.connect(self.usersChanged)
        self.usersChanged.connect(self.usernameChanged)
        self.usernameChanged.connect(self.playersChanged)

    @Property(str, notify=usernameChanged)
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username
        self.usernameChanged.emit()

    @Property(list, constant=True)
    def leagues(self):
        return [league['name'] for league in self._master.context.sleeper.user_leagues]

    @Property(list, notify=usersChanged)
    def users(self):
        league = League(self._master.context, self._league)
        return [user['display_name'] for user in league.users]

    @Property(str, notify=leagueChanged)
    def league(self):
        return self._league

    @league.setter
    def league(self, league):
        self._league = league
        league = League(self._master.context, self._league)
        users = [user['display_name'] for user in league.users]
        if self._username not in users:
            self._username = users[0]
        self.leagueChanged.emit()

    @Property(str, notify=playersChanged)
    def players(self):
        team = Team(self._master.context, self._username, self._league)
        return json.dumps(team.players)


