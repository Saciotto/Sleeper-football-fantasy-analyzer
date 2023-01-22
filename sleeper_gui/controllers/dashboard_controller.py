import traceback
from PySide6.QtCore import QObject, Signal, Slot
from threading import Thread


class DashboardController(QObject):
    updateCompleted = Signal()
    updateFailed = Signal()

    def __init__(self, parent):
        QObject.__init__(self, parent)
        self._sleeper = parent.sleeper
        self._master = parent

    @Slot(result=str)
    def lastUpdate(self):
        return self._sleeper.last_download.ctime()

    @Slot(str)
    def update(self):
        thread = Thread(target=self._execute_update)
        thread.start()

    def _execute_update(self):
        username = self._sleeper.db.username
        try:
            self._sleeper.download(username)
            self.updateCompleted.emit()
        except Exception:
            print(traceback.format_exc())
            self.updateFailed.emit()
