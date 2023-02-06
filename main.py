from data_base.db import DataBase
from datetime import date, timedelta
from decimal import Decimal
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
    # db.beautify_items(db.get_item())


if __name__ == '__main__':
    main()
