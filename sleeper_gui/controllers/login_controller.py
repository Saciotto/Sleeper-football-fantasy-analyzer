import traceback
from PySide6.QtCore import QObject, Signal, Property, Slot
from threading import Thread


class LoginController(QObject):
    def __init__(self, parent):
        QObject.__init__(self, parent)
        self._master = parent
        self._logged = self._master.context.username is not None

    def _is_logged(self):
        return self._logged

    def _execute_login(self, username):
        if self._logged:
            return
        try:
            self._master.sleeper.download_statistics(username)
            self._master.context.username = username
            self._logged = True
            # noinspection PyUnresolvedReferences
            self.loggedChanged.emit()
        except Exception:
            print(traceback.format_exc())
            # noinspection PyUnresolvedReferences
            self.loginFailed.emit()

    @Slot(str)
    def login(self, username):
        thread = Thread(target=self._execute_login, args=(username,))
        thread.start()

    loggedChanged = Signal()
    loginFailed = Signal()

    logged = Property(bool, _is_logged, notify=loggedChanged)
