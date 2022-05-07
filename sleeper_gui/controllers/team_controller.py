from PySide6.QtCore import QObject, Signal, Property, Slot
from sleeper_analyzer.models.team import Team


class TeamController(QObject):
    def __init__(self, parent):
        QObject.__init__(self, parent)
        self._master = parent

    def _get_players(self):
        team = Team(self._master.context, self._master.context.username, self._master.context.default_league)
        return '\n'.join([str(player) for player in team.players])

    playersChanged = Signal()

    players = Property(str, _get_players, notify=playersChanged)
