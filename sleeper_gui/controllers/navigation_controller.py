from PySide6.QtCore import QObject, Signal


class NavigationController(QObject):
    goDashboardView = Signal()
    goTeamView = Signal()
    goBestLineupView = Signal()

    def __init__(self, parent):
        QObject.__init__(self, parent)
