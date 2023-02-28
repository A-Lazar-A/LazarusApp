from PySide6 import QtGui

from data_base.db import DataBase
from ui.mainwindow import MainWindow
from ui.splashwindow import SplashWindow
from PySide6.QtWidgets import QApplication
import sys


def main():
    db = DataBase()
    db.create_table()
    app = QApplication()
    app.setWindowIcon(QtGui.QIcon('favicon.ico'))

    window = MainWindow()
    splash = SplashWindow(window)

    splash.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
