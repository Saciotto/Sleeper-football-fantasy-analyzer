import traceback
from PySide6.QtCore import QObject, Signal, Property, Slot
from threading import Thread


# noinspection PyUnresolvedReferences
class LoginController(QObject):
    loggedChanged = Signal()
    loginFailed = Signal()

    def __init__(self, parent):
        QObject.__init__(self, parent)
        self._context = parent.context
        self._sleeper = parent.sleeper
        self._logged = self._context.username is not None

    @Property(bool, notify=loggedChanged)
    def logged(self):
        return self._logged

    @Slot(str)
    def login(self, username):
        thread = Thread(target=self._execute_login, args=(username,))
        thread.start()

    def _execute_login(self, username):
        if self._logged:
            return
        try:
            self._sleeper.download_statistics(username)
            self._context.username = username
            self._logged = True
            self.loggedChanged.emit()
        except Exception:
            print(traceback.format_exc())
            self.loginFailed.emit()
