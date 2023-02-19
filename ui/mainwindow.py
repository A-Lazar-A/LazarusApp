from PySide6.QtWidgets import QMainWindow, QDialog, QTableWidgetItem, QHeaderView
from PySide6.QtGui import QColor

from ui.base.ui_main import Ui_MainWindow
from ui.dialogwindow import DialogWindow
from ui.solddialogwindow import SoldDialogWindow
from data_base.db import DataBase


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.add_button.clicked.connect(self.open_add_dialog)
        self.ui.delete_button.clicked.connect(self.delete_items)
        self.ui.sold_button.clicked.connect(self.open_sold_dialog)
        self.refresh_table()
        self.refresh_weekly()
        self.refresh_monthly()
        self.refresh_yearly()
        self.refresh_all_income()

    def refresh_table(self):
        db = DataBase()
        self.ui.table_items_view.setRowCount(0)

        columns = db.get_number_of_columns() - 1
        self.ui.table_items_view.setColumnCount(columns)

        res = db.beautify_items(db, db.get_item())
        for row_number, row_data in enumerate(res):
            self.ui.table_items_view.insertRow(row_number)
            for colum, data in enumerate(row_data):
                self.ui.table_items_view.setItem(row_number, colum, QTableWidgetItem(data))
                if colum == 5 or colum == 6:
                    if float(data[:-1]) >= 0:
                        self.ui.table_items_view.item(row_number, colum).setBackground(QColor(87, 227, 137, 50))
                    else:
                        self.ui.table_items_view.item(row_number, colum).setBackground(QColor(165, 29, 45, 50))
        self.ui.table_items_view.setColumnHidden(columns - 1, True)
        header = self.ui.table_items_view.horizontalHeader()
        for i in range(columns):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)

    def delete_items(self):
        db = DataBase()
        selected = self.ui.table_items_view.selectedIndexes()
        for sel in selected:
            rowid = self.ui.table_items_view.item(sel.row(), 7).text()
            db.delete_item(rowid)
        self.refresh_table()
        self.refresh_weekly()
        self.refresh_monthly()
        self.refresh_yearly()
        self.refresh_all_income()

    def refresh_weekly(self):
        db = DataBase()
        rub, usd = db.calc_income(db.get_sales(7))
        self.ui.weekly_income_rub.setText(str(rub) + ' ₽')
        self.ui.weekly_income_usd.setText(str(usd) + ' $')
        self.color_income(self.ui.weekly_income_rub, rub)
        self.color_income(self.ui.weekly_income_usd, usd)

    def refresh_monthly(self):
        db = DataBase()
        rub, usd = db.calc_income(db.get_sales(30))
        self.ui.monthly_income_rub.setText(str(rub) + ' ₽')
        self.ui.monthly_income_usd.setText(str(usd) + ' $')
        self.color_income(self.ui.monthly_income_rub, rub)
        self.color_income(self.ui.monthly_income_usd, usd)

    def refresh_yearly(self):
        db = DataBase()
        rub, usd = db.calc_income(db.get_sales(365))
        self.ui.yearly_income_rub.setText(str(rub) + ' ₽')
        self.ui.yearly_income_usd.setText(str(usd) + ' $')
        self.color_income(self.ui.yearly_income_rub, rub)
        self.color_income(self.ui.yearly_income_usd, usd)

    def refresh_all_income(self):
        db = DataBase()
        rub, usd = db.calc_income(db.get_item())
        self.ui.all_income_rub.setText(str(rub) + ' ₽')
        self.ui.all_income_usd.setText(str(usd) + ' $')
        self.color_income(self.ui.all_income_rub, rub)
        self.color_income(self.ui.all_income_usd, usd)

    def color_income(self, label, income):
        if income >= 0:
            label.setStyleSheet('background-color: rgba(87, 227, 137, 50)')
        else:
            label.setStyleSheet('background-color: rgba(165, 29, 45, 50)')

    def open_add_dialog(self):
        d_window = DialogWindow(self)
        d_window.exec_()

    def open_sold_dialog(self):
        selected = self.ui.table_items_view.selectedIndexes()
        if not selected:
            return
        d_window = SoldDialogWindow(self, selected)
        d_window.exec_()
