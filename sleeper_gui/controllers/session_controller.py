import traceback
from PySide6.QtCore import QObject, Signal, Property, Slot
from threading import Thread


class SessionController(QObject):
    loggedChanged = Signal()
    loginFailed = Signal()

    def __init__(self, parent):
        QObject.__init__(self, parent)
        self._sleeper = parent.sleeper

    @Property(bool, notify=loggedChanged)
    def logged(self):
        return self._sleeper.db.initialized

    @Slot(str)
    def login(self, username):
        thread = Thread(target=self._execute_login, args=(username,))
        thread.start()

    def _execute_login(self, username):
        if self._logged:
            return
        try:
            self._sleeper.download(username)
            self.loggedChanged.emit()
        except Exception:
            print(traceback.format_exc())
            self.loginFailed.emit()
