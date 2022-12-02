from PySide6.QtCore import QObject, Property

from sleeper_gui.controllers.navigation_controller import NavigationController
from sleeper_gui.controllers.login_controller import LoginController
from sleeper_gui.controllers.team_controller import TeamController
from sleeper_gui.controllers.dashboard_controller import DashboardController
from sleeper_analyzer.context import Context
from sleeper_analyzer.sleeper import Sleeper


class ApplicationController(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.context = Context()
        self.sleeper = Sleeper()
        self.login_controller = LoginController(self)
        self.navigation_controller = NavigationController(self)
        self.team_controller = TeamController(self)
        self.dashboard_controller = DashboardController(self)

    @Property(LoginController, constant=True)
    def loginController(self):
        return self.login_controller

    @Property(NavigationController, constant=True)
    def navigationController(self):
        return self.navigation_controller

    @Property(TeamController, constant=True)
    def teamController(self):
        return self.team_controller

    @Property(DashboardController, constant=True)
    def dashboardController(self):
        return self.dashboard_controller
