from PySide6.QtCore import QObject, Property

from sleeper_gui.controllers.navigation_controller import NavigationController
from sleeper_gui.controllers.session_controller import SessionController
from sleeper_gui.controllers.team_controller import TeamController
from sleeper_gui.controllers.dashboard_controller import DashboardController
from sleeper_analyzer.sleeper import Sleeper


class ApplicationController(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.sleeper = Sleeper()
        self.session_controller = SessionController(self)
        self.navigation_controller = NavigationController(self)
        self.team_controller = TeamController(self)
        self.dashboard_controller = DashboardController(self)
        self.session_controller.loggedChanged.connect(self.team_controller.update)
        if self.sleeper.db.initialized:
            self.team_controller.update()

    @Property(SessionController, constant=True)
    def session(self):
        return self.session_controller

    @Property(NavigationController, constant=True)
    def navigation(self):
        return self.navigation_controller

    @Property(TeamController, constant=True)
    def team(self):
        return self.team_controller

    @Property(DashboardController, constant=True)
    def dashboard(self):
        return self.dashboard_controller
