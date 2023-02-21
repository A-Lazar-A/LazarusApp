from PySide6.QtWidgets import QDialog
from datetime import date

from ui.base.ui_dialog_sold import Ui_sold_dialog
from decimal import Decimal
from data_base.db import DataBase


class SoldDialogWindow(QDialog):

    def __init__(self, mainwindow, selected):
        super(SoldDialogWindow, self).__init__()
        db = DataBase()
        self.ui = Ui_sold_dialog()
        self.mainwindow = mainwindow
        self.selected = selected
        self.ui.setupUi(self)
        self.ui.sold_date_ui.setDate(date.today())
        self.setWindowTitle(self.mainwindow.ui.table_items_view.item(self.selected[0].row(), 0).text())
        rowid = self.mainwindow.ui.table_items_view.item(self.selected[0].row(), 9).text()
        item = db.get_item(rowid)
        self.ui.sold_creator_royalty.setValue(item[7])
        self.ui.sold_market_royalty.setValue(item[8])
        self.ui.sold_dialog_button.clicked.connect(self.sold_item)

# TODO: Add royalties and autofill off fields
    def sold_item(self):
        db = DataBase()

        item = {
            'id': self.mainwindow.ui.table_items_view.item(self.selected[0].row(), 7).text(),
            'sell_price': Decimal(self.ui.sold_price_ui.text().replace(',', '.')),
            'sell_currency': self.ui.sold_currency_ui.currentText().lower(),
            'sell_date': self.ui.sold_date_ui.date().toString('yyyy-MM-dd'),
            'creator_royalty': Decimal(self.ui.sold_creator_royalty.text().replace(', ', '.')),
            'market_royalty': Decimal(self.ui.sold_market_royalty.text().replace(',', '.')),
        }

        db.update_sold_item(item)

        self.mainwindow.refresh_table()
        self.mainwindow.refresh_weekly()
        self.mainwindow.refresh_monthly()
        self.mainwindow.refresh_yearly()
        self.mainwindow.refresh_all_income()
        self.close()
