import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication
from PySide6.QtQuick import QQuickView

from __feature__ import snake_case, true_property

from . import views_rc


def main():
    app = QApplication()
    view = QQuickView()

    view.source = 'qrc:/views/LoginView.qml'
    view.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
