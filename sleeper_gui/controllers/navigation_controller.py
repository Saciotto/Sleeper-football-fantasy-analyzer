from PySide6.QtCore import QObject, Signal, Property


class NavigationController(QObject):

    def __init__(self, parent):
        QObject.__init__(self, parent)
        self._master_controller = parent

    goDashboardView = Signal()
    goTeamView = Signal()
    goBestLineupView = Signal()
