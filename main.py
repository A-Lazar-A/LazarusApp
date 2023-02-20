from data_base.db import DataBase
from ui.mainwindow import MainWindow
from PySide6.QtWidgets import QApplication
import sys


def main():
    db = DataBase()
    db.create_table()
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
