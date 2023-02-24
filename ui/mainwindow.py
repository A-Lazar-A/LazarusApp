from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView
from PySide6.QtGui import QColor
from PySide6 import QtCharts
from PySide6.QtCharts import QAbstractBarSeries
import locale

from datetime import date
from ui.base.ui_main import Ui_MainWindow
from ui.dialogwindow import DialogWindow
from ui.solddialogwindow import SoldDialogWindow
from data_base.db import DataBase


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.add_button.clicked.connect(self.open_add_dialog)
        self.ui.delete_button.clicked.connect(self.delete_items)
        self.ui.sold_button.clicked.connect(self.open_sold_dialog)

        self.whole_chart()
        self.weekly_chart()
        self.monthly_chart()
        self.yearly_chart()

        self.refresh_table()
        self.refresh_weekly()
        self.refresh_monthly()
        self.refresh_yearly()
        self.refresh_all_income()

    def set_chart_style(self, chart):
        chart.axisY().setLabelsColor(QColor('white'))
        chart.axisY().setTitleText('USD')
        chart.axisY().setTitleBrush(QColor('white'))
        chart.legend().setVisible(False)
        chart.legend().setLabelColor('white')
        chart.layout().setContentsMargins(0, 0, 0, 0)
        chart.setBackgroundRoundness(0)
        chart.setBackgroundBrush(QColor(80, 80, 80))

    def weekly_chart(self):
        db = DataBase()
        usd_income = QtCharts.QBarSet('USD')
        rub_income = QtCharts.QBarSet('RUB')
        usd_income.setColor(QColor(57, 57, 57))
        rub_income.setColor(QColor(128, 143, 133))
        income_calender = {}
        items = db.get_sales(date.today().weekday())
        dates = []
        for item in items:
            sell_date = date.fromisoformat(item[6])
            if sell_date not in income_calender:
                income_calender[sell_date] = [item[-2], item[-3]]
            else:
                income_calender[sell_date][0] += item[-2]
                income_calender[sell_date][1] += item[-3]
        for weekday, income in sorted(income_calender.items()):
            dates.append(weekday.strftime('%A'))
            usd_income.append(income[0])
            rub_income.append(income[1])
        series = QtCharts.QBarSeries()
        # Do I need RUB? IDK
        series.append([usd_income])
        series.setLabelsVisible(True)
        series.setLabelsAngle(270)
        series.setLabelsPosition(QAbstractBarSeries.LabelsPosition.LabelsOutsideEnd)

        chart = QtCharts.QChart()

        chart.addSeries(series)

        axis = QtCharts.QBarCategoryAxis()
        axis.append(dates)
        axis.setLabelsColor(QColor('white'))
        chart.createDefaultAxes()
        chart.setAxisX(axis)
        self.set_chart_style(chart)
        self.ui.weekly_chart.setChart(chart)

    def monthly_chart(self):
        db = DataBase()
        usd_income = QtCharts.QBarSet('USD')
        rub_income = QtCharts.QBarSet('RUB')
        usd_income.setColor(QColor(57, 57, 57))
        rub_income.setColor(QColor(128, 143, 133))
        income_calender = {}
        items = db.get_sales(date.today().day)
        dates = []
        for item in items:
            sell_date = date.fromisoformat(item[6])
            if sell_date not in income_calender:
                income_calender[sell_date] = [item[-2], item[-3]]
            else:
                income_calender[sell_date][0] += item[-2]
                income_calender[sell_date][1] += item[-3]
        for month_year, income in sorted(income_calender.items()):
            dates.append(month_year.strftime('%d.%m'))
            usd_income.append(income[0])
            rub_income.append(income[1])

        series = QtCharts.QBarSeries()
        # Do I need RUB? IDK
        series.append([usd_income])
        series.setLabelsVisible(True)
        series.setLabelsAngle(270)
        series.setLabelsPosition(QAbstractBarSeries.LabelsPosition.LabelsOutsideEnd)

        chart = QtCharts.QChart()

        chart.addSeries(series)

        axis = QtCharts.QBarCategoryAxis()
        axis.append(dates)
        axis.setLabelsColor(QColor('white'))
        chart.createDefaultAxes()
        chart.setAxisX(axis)

        self.set_chart_style(chart)

        self.ui.monthly_chart.setChart(chart)

    def yearly_chart(self):
        db = DataBase()
        usd_income = QtCharts.QBarSet('USD')
        rub_income = QtCharts.QBarSet('RUB')
        usd_income.setColor(QColor(57, 57, 57))
        rub_income.setColor(QColor(128, 143, 133))
        income_calender = {}
        delta = date.today() - date.today().replace(day=1, month=1)
        items = db.get_sales(delta.days)
        dates = []
        for item in items:
            sell_date = date.fromisoformat(item[6]).replace(day=1)
            if sell_date not in income_calender:
                income_calender[sell_date] = [item[-2], item[-3]]
            else:
                income_calender[sell_date][0] += item[-2]
                income_calender[sell_date][1] += item[-3]
        for month_year, income in sorted(income_calender.items()):
            dates.append(month_year.strftime('%B'))
            usd_income.append(income[0])
            rub_income.append(income[1])

        series = QtCharts.QBarSeries()
        # Do I need RUB? IDK
        series.append([usd_income])
        series.setLabelsVisible(True)
        series.setLabelsAngle(270)
        series.setLabelsPosition(QAbstractBarSeries.LabelsPosition.LabelsOutsideEnd)

        chart = QtCharts.QChart()

        chart.addSeries(series)

        axis = QtCharts.QBarCategoryAxis()
        axis.append(dates)
        axis.setLabelsColor(QColor('white'))
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)

        self.set_chart_style(chart)

        self.ui.yearly_chart.setChart(chart)

    def whole_chart(self):
        db = DataBase()
        usd_income = QtCharts.QBarSet('USD')
        rub_income = QtCharts.QBarSet('RUB')
        usd_income.setColor(QColor(57, 57, 57))
        rub_income.setColor(QColor(128, 143, 133))
        income_calender = {}
        items = db.get_item()
        dates = []
        for item in items:
            sell_date = date.fromisoformat(item[6]).replace(day=1)
            if sell_date not in income_calender:
                income_calender[sell_date] = [item[-2], item[-3]]
            else:
                income_calender[sell_date][0] += item[-2]
                income_calender[sell_date][1] += item[-3]
        for month_year, income in sorted(income_calender.items()):
            dates.append(month_year.strftime('%m.%y'))
            usd_income.append(income[0])
            rub_income.append(income[1])

        series = QtCharts.QBarSeries()
        # Do I need RUB? IDK
        series.append([usd_income])
        series.setLabelsVisible(True)
        series.setLabelsAngle(270)
        series.setLabelsPosition(QAbstractBarSeries.LabelsPosition.LabelsOutsideEnd)

        chart = QtCharts.QChart()

        chart.addSeries(series)

        axis = QtCharts.QBarCategoryAxis()
        axis.append(dates)
        axis.setLabelsColor(QColor('white'))
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)

        self.set_chart_style(chart)

        self.ui.whole_chart.setChart(chart)

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
                if colum == 7 or colum == 8:
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
            rowid = self.ui.table_items_view.item(sel.row(), 9).text()
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
