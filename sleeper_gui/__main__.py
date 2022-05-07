import sys
import os
from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, qmlRegisterType

from sleeper_gui.helpers import get_qrc_root, enable_qml_logs, compile_resources
from sleeper_gui.controllers.master_controller import MasterController
from sleeper_gui.controllers.navigation_controller import NavigationController
from sleeper_gui.controllers.login_controller import LoginController
from sleeper_gui.controllers.team_controller import TeamController

compile_resources()

# noinspection PyUnresolvedReferences
import sleeper_gui.resources.assets_rc
# noinspection PyUnresolvedReferences
import sleeper_gui.resources.components_rc
# noinspection PyUnresolvedReferences
import sleeper_gui.resources.views_rc


# noinspection PyTypeChecker
def main():
    enable_qml_logs()

    os.environ['QT_QUICK_CONTROLS_STYLE'] = "Material"
    os.environ['QT_QUICK_CONTROLS_MATERIAL_THEME'] = "Dark"
    os.environ['QT_QUICK_CONTROLS_MATERIAL_VARIANT'] = "Dense"
    os.environ['QT_QUICK_CONTROLS_MATERIAL_ACCENT'] = "Indigo"

    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    qrc_root = get_qrc_root()
    engine.addImportPath(qrc_root)

    qmlRegisterType(MasterController, 'Sleeper', 1, 0, 'MasterController')
    qmlRegisterType(NavigationController, 'Sleeper', 1, 0, 'NavigationController')
    qmlRegisterType(LoginController, 'Sleeper', 1, 0, 'LoginController')
    qmlRegisterType(TeamController, 'Sleeper', 1, 0, 'TeamController')

    controller = MasterController()
    engine.rootContext().setContextProperty("masterController", controller)

    engine.load(QUrl('qrc:/views/MasterView.qml'))
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
