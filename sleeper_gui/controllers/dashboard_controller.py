import traceback
from PySide6.QtCore import QObject, Signal, Slot
from threading import Thread


class DashboardController(QObject):
    updateCompleted = Signal()
    updateFailed = Signal()

    def __init__(self, parent):
        QObject.__init__(self, parent)
        self._context = parent.context
        self._sleeper = parent.sleeper
        self._master = parent

    @Slot(result=str)
    def lastUpdate(self):
        return self._context.last_update.ctime()

    @Slot(str)
    def update(self):
        thread = Thread(target=self._execute_update)
        thread.start()

    def _execute_update(self):
        username = self._context.username
        try:
            self._sleeper.download_statistics(username)
            self._context.update()
            self.updateCompleted.emit()
        except Exception:
            print(traceback.format_exc())
            self.updateFailed.emit()
