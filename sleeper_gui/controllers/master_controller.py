from PySide6.QtCore import QObject, Property

from sleeper_gui.controllers.navigation_controller import NavigationController
from sleeper_analyzer.context import Context


class MasterController(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.context = Context()
        self._navigation_controller = NavigationController(self)

    def get_navigation_controller(self):
        return self._navigation_controller

    navigationController = Property(NavigationController, get_navigation_controller, constant=True)
