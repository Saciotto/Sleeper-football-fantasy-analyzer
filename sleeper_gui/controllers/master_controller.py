from PySide6.QtCore import QObject, Property

from sleeper_gui.controllers.navigation_controller import NavigationController
from sleeper_gui.controllers.login_controller import LoginController
from sleeper_gui.controllers.team_controller import TeamController
from sleeper_analyzer.context import Context
from sleeper_analyzer.sleeper import Sleeper


class MasterController(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.context = Context()
        self.sleeper = Sleeper()
        self.login_controller = LoginController(self)
        self.navigation_controller = NavigationController(self)
        self.team_controller = TeamController(self)

    def get_login_controller(self):
        return self.login_controller

    def get_navigation_controller(self):
        return self.navigation_controller

    def get_team_controller(self):
        return self.team_controller

    loginController = Property(LoginController, get_login_controller, constant=True)
    navigationController = Property(NavigationController, get_navigation_controller, constant=True)
    teamController = Property(TeamController, get_team_controller, constant=True)

