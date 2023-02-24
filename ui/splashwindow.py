from PySide6 import QtCore
from PySide6.QtWidgets import QMainWindow

from ui.base.ui_splash import Ui_SplashWindow


class SplashWindow(QMainWindow):

    def __init__(self, mainwindow):
        super(SplashWindow, self).__init__()
        self.ui = Ui_SplashWindow()
        self.mainwindow = mainwindow
        self.ui.setupUi(self)
        self.counter = 0
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)

    def progress(self):
        self.ui.progressBar.setValue(self.counter)
        if self.counter > 100:
            self.timer.stop()

            self.mainwindow.show()
            self.close()

        self.counter += 1
