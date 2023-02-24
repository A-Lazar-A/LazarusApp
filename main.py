from PySide6.QtGui import QScreen

from data_base.db import DataBase
from ui.mainwindow import MainWindow
from ui.splashwindow import SplashWindow
from PySide6.QtWidgets import QApplication
import sys


def main():
    db = DataBase()
    db.create_table()
    app = QApplication()
    centered = QScreen.availableGeometry(QApplication.primaryScreen()).center()

    window = MainWindow()
    splash = SplashWindow(window)

    splash.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
