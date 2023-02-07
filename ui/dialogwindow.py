from PySide6.QtWidgets import QDialog
from datetime import date

from ui.base.ui_dialog import Ui_Dialog
from decimal import Decimal
from data_base.db import DataBase


class DialogWindow(QDialog):

    def __init__(self, mainwindow):
        super(DialogWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.mainwindow = mainwindow
        self.ui.setupUi(self)
        self.ui.buy_date_ui.setDate(date.today())
        self.ui.sell_date_ui.setDate(date.today())
        self.ui.add_dialog_button.clicked.connect(self.add_item)

    def add_item(self):
        db = DataBase()
        name = self.ui.item_name.text()
        if name == '':
            print('null name')
            return

        item = {
            'name': name,
            'buy_price': Decimal(self.ui.buy_price_ui.text().replace(',', '.')),
            'buy_currency': self.ui.buy_currency_ui.currentText().lower(),
            'sell_price': Decimal(self.ui.sell_price_ui.text().replace(',', '.')),
            'sell_currency': self.ui.sell_currency_ui.currentText().lower(),
            'buy_date': self.ui.buy_date_ui.date().toString('yyyy-MM-dd'),
            'sell_date': self.ui.sell_date_ui.date().toString('yyyy-MM-dd'),
            'income_rub': None,
            'income_usd': None,
        }
        db.add_item(item, int(self.ui.quantity_ui.text()))
        self.mainwindow.refresh_table()
        self.mainwindow.refresh_weekly()
        self.mainwindow.refresh_monthly()
        self.mainwindow.refresh_yearly()
        self.mainwindow.refresh_all_income()
