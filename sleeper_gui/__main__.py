import sys
import os
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, qmlRegisterType

from sleeper_gui.helpers import get_qml_root, enable_qml_logs, get_view
from sleeper_gui.controllers.master_controller import ApplicationController
from sleeper_gui.controllers.navigation_controller import NavigationController
from sleeper_gui.controllers.login_controller import LoginController
from sleeper_gui.controllers.team_controller import TeamController
from sleeper_gui.controllers.dashboard_controller import DashboardController


def main():
    enable_qml_logs()

    os.environ['QT_QUICK_CONTROLS_STYLE'] = "Material"
    os.environ['QT_QUICK_CONTROLS_MATERIAL_THEME'] = "Dark"
    os.environ['QT_QUICK_CONTROLS_MATERIAL_ACCENT'] = "Indigo"

    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    qml_root = get_qml_root()
    engine.addImportPath(qml_root)

    qmlRegisterType(ApplicationController, 'Sleeper', 1, 0, 'ApplicationController')
    qmlRegisterType(NavigationController, 'Sleeper', 1, 0, 'NavigationController')
    qmlRegisterType(LoginController, 'Sleeper', 1, 0, 'LoginController')
    qmlRegisterType(TeamController, 'Sleeper', 1, 0, 'TeamController')
    qmlRegisterType(DashboardController, 'Sleeper', 1, 0, 'DashboardController')

    controller = ApplicationController()
    engine.rootContext().setContextProperty("app", controller)

    master_view = get_view('MasterView.qml')
    engine.load(master_view)
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
