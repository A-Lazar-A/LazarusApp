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

    geo = window.frameGeometry()
    geo.moveCenter(centered)
    window.move(geo.topLeft())
    geo = splash.frameGeometry()
    geo.moveCenter(centered)
    splash.move(geo.topRight())
    splash.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
