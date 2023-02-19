# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 700)
        MainWindow.setMinimumSize(QSize(1200, 700))
        MainWindow.setStyleSheet(u"background-color: rgb(31, 31, 31);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.income_frame = QFrame(self.centralwidget)
        self.income_frame.setObjectName(u"income_frame")
        self.income_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 5px;")
        self.verticalLayout = QVBoxLayout(self.income_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.income_frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.all_income_rub = QLabel(self.income_frame)
        self.all_income_rub.setObjectName(u"all_income_rub")
        font1 = QFont()
        font1.setPointSize(16)
        self.all_income_rub.setFont(font1)

        self.horizontalLayout_4.addWidget(self.all_income_rub)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.all_income_usd = QLabel(self.income_frame)
        self.all_income_usd.setObjectName(u"all_income_usd")
        self.all_income_usd.setFont(font1)

        self.horizontalLayout_4.addWidget(self.all_income_usd)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.label_2 = QLabel(self.income_frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(0, 41))

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.weekly_income_rub = QLabel(self.income_frame)
        self.weekly_income_rub.setObjectName(u"weekly_income_rub")
        font2 = QFont()
        font2.setPointSize(18)
        self.weekly_income_rub.setFont(font2)

        self.horizontalLayout.addWidget(self.weekly_income_rub)

        self.weekly_income_usd = QLabel(self.income_frame)
        self.weekly_income_usd.setObjectName(u"weekly_income_usd")
        self.weekly_income_usd.setFont(font2)

        self.horizontalLayout.addWidget(self.weekly_income_usd)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_3 = QLabel(self.income_frame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.monthly_income_rub = QLabel(self.income_frame)
        self.monthly_income_rub.setObjectName(u"monthly_income_rub")
        self.monthly_income_rub.setFont(font2)

        self.horizontalLayout_2.addWidget(self.monthly_income_rub)

        self.monthly_income_usd = QLabel(self.income_frame)
        self.monthly_income_usd.setObjectName(u"monthly_income_usd")
        self.monthly_income_usd.setFont(font2)

        self.horizontalLayout_2.addWidget(self.monthly_income_usd)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_4 = QLabel(self.income_frame)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.yearly_income_rub = QLabel(self.income_frame)
        self.yearly_income_rub.setObjectName(u"yearly_income_rub")
        self.yearly_income_rub.setFont(font2)

        self.horizontalLayout_3.addWidget(self.yearly_income_rub)

        self.yearly_income_usd = QLabel(self.income_frame)
        self.yearly_income_usd.setObjectName(u"yearly_income_usd")
        self.yearly_income_usd.setFont(font2)

        self.horizontalLayout_3.addWidget(self.yearly_income_usd)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_6.addWidget(self.income_frame)

        self.statistic_frame = QFrame(self.centralwidget)
        self.statistic_frame.setObjectName(u"statistic_frame")
        self.statistic_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 5px;")
        self.verticalLayout_2 = QVBoxLayout(self.statistic_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 11, -1, -1)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_13 = QLabel(self.statistic_frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"background-color: none;\n"
"border: none;")

        self.horizontalLayout_5.addWidget(self.label_13)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.tabWidget = QTabWidget(self.statistic_frame)
        self.tabWidget.setObjectName(u"tabWidget")
        font3 = QFont()
        font3.setPointSize(13)
        self.tabWidget.setFont(font3)
        self.tabWidget.setStyleSheet(u"background-color: rgb(31, 31, 31);\n"
"border: none;")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.whole_time = QWidget()
        self.whole_time.setObjectName(u"whole_time")
        self.label_14 = QLabel(self.whole_time)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(90, 110, 67, 17))
        self.tabWidget.addTab(self.whole_time, "")
        self.weekly = QWidget()
        self.weekly.setObjectName(u"weekly")
        self.label_15 = QLabel(self.weekly)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(100, 60, 67, 17))
        self.tabWidget.addTab(self.weekly, "")
        self.monthly = QWidget()
        self.monthly.setObjectName(u"monthly")
        self.label_16 = QLabel(self.monthly)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(150, 70, 67, 17))
        self.tabWidget.addTab(self.monthly, "")
        self.yearly = QWidget()
        self.yearly.setObjectName(u"yearly")
        self.label_17 = QLabel(self.yearly)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(250, 120, 67, 17))
        self.tabWidget.addTab(self.yearly, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.horizontalLayout_6.addWidget(self.statistic_frame)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.add_button = QPushButton(self.centralwidget)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setMinimumSize(QSize(0, 40))
        self.add_button.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: rgba(255, 255, 255, 50);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/add_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_button.setIcon(icon)

        self.horizontalLayout_7.addWidget(self.add_button)

        self.sold_button = QPushButton(self.centralwidget)
        self.sold_button.setObjectName(u"sold_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sold_button.sizePolicy().hasHeightForWidth())
        self.sold_button.setSizePolicy(sizePolicy1)
        self.sold_button.setMinimumSize(QSize(0, 40))
        self.sold_button.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: rgba(255, 255, 255, 50);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/done_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sold_button.setIcon(icon1)

        self.horizontalLayout_7.addWidget(self.sold_button)

        self.delete_button = QPushButton(self.centralwidget)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setMinimumSize(QSize(0, 40))
        self.delete_button.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: rgba(255, 255, 255, 50);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/delete_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_button.setIcon(icon2)

        self.horizontalLayout_7.addWidget(self.delete_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.table_items_view = QTableWidget(self.centralwidget)
        if (self.table_items_view.columnCount() < 7):
            self.table_items_view.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_items_view.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_items_view.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_items_view.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_items_view.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_items_view.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_items_view.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_items_view.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.table_items_view.setObjectName(u"table_items_view")
        self.table_items_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table_items_view.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_items_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_items_view.horizontalHeader().setVisible(True)
        self.table_items_view.horizontalHeader().setCascadingSectionResizes(False)
        self.table_items_view.horizontalHeader().setHighlightSections(True)
        self.table_items_view.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.table_items_view)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"LazarusApp", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Income", None))
        self.all_income_rub.setText(QCoreApplication.translate("MainWindow", u"rub", None))
        self.all_income_usd.setText(QCoreApplication.translate("MainWindow", u"usd", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Weekly", None))
        self.weekly_income_rub.setText(QCoreApplication.translate("MainWindow", u"rub", None))
        self.weekly_income_usd.setText(QCoreApplication.translate("MainWindow", u"usd", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Monthly", None))
        self.monthly_income_rub.setText(QCoreApplication.translate("MainWindow", u"rub", None))
        self.monthly_income_usd.setText(QCoreApplication.translate("MainWindow", u"usd", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Yearly", None))
        self.yearly_income_rub.setText(QCoreApplication.translate("MainWindow", u"rub", None))
        self.yearly_income_usd.setText(QCoreApplication.translate("MainWindow", u"usd", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Statistic", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Chart", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.whole_time), QCoreApplication.translate("MainWindow", u"Whole Time", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Chart", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.weekly), QCoreApplication.translate("MainWindow", u"Weekly", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Chart", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.monthly), QCoreApplication.translate("MainWindow", u"Monthly", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Chart", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.yearly), QCoreApplication.translate("MainWindow", u"Yearly", None))
        self.add_button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.sold_button.setText(QCoreApplication.translate("MainWindow", u"Sold", None))
        self.delete_button.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        ___qtablewidgetitem = self.table_items_view.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.table_items_view.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        ___qtablewidgetitem2 = self.table_items_view.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Sell Price", None));
        ___qtablewidgetitem3 = self.table_items_view.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Purchase Date", None));
        ___qtablewidgetitem4 = self.table_items_view.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Sell Date", None));
        ___qtablewidgetitem5 = self.table_items_view.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Income RUB", None));
        ___qtablewidgetitem6 = self.table_items_view.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Income USD", None));
    # retranslateUi

