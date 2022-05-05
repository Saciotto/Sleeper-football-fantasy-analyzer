from PySide6.QtCore import QObject, Signal, Property


class NavigationController(QObject):

    def __init__(self, parent):
        QObject.__init__(self, parent)
        self._master_controller = parent
        self._logged = self._master_controller.context.username is not None

    def is_logged(self):
        #return self._logged
        return False

    def refresh(self):
        logged = self._master_controller.context.username is not None
        if self._logged != logged:
            self._logged = logged
            # noinspection PyUnresolvedReferences
            self.loggedChanged.emit()

    loggedChanged = Signal()
    goDashboardView = Signal()
    goTeamView = Signal()
    goBestLineupView = Signal()

    isLogged = Property(bool, is_logged, notify=loggedChanged)
