# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialog_sold.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDialog, QDoubleSpinBox, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_sold_dialog(object):
    def setupUi(self, sold_dialog):
        if not sold_dialog.objectName():
            sold_dialog.setObjectName(u"sold_dialog")
        sold_dialog.resize(530, 260)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sold_dialog.sizePolicy().hasHeightForWidth())
        sold_dialog.setSizePolicy(sizePolicy)
        sold_dialog.setMinimumSize(QSize(530, 0))
        sold_dialog.setStyleSheet(u"background-color: rgb(31, 31, 31);\n"
"color: rgb(255, 255, 255);")
        self.horizontalLayout_3 = QHBoxLayout(sold_dialog)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame = QFrame(sold_dialog)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.sell_frame = QFrame(self.frame)
        self.sell_frame.setObjectName(u"sell_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sell_frame.sizePolicy().hasHeightForWidth())
        self.sell_frame.setSizePolicy(sizePolicy1)
        self.sell_frame.setStyleSheet(u"QFrame{\n"
"background-color: none;\n"
"border:none;\n"
"}\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.sell_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.label_4 = QLabel(self.sell_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setStyleSheet(u"background-color: none;\n"
"border: none;")

        self.verticalLayout_4.addWidget(self.label_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sold_price_ui = QDoubleSpinBox(self.sell_frame)
        self.sold_price_ui.setObjectName(u"sold_price_ui")
        self.sold_price_ui.setStyleSheet(u"font-size: 20pt;\n"
"")
        self.sold_price_ui.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sold_price_ui.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.sold_price_ui.setDecimals(4)
        self.sold_price_ui.setMaximum(99999999999999991611392.000000000000000)
        self.sold_price_ui.setStepType(QAbstractSpinBox.DefaultStepType)

        self.horizontalLayout.addWidget(self.sold_price_ui)

        self.sold_currency_ui = QComboBox(self.sell_frame)
        self.sold_currency_ui.addItem("")
        self.sold_currency_ui.addItem("")
        self.sold_currency_ui.addItem("")
        self.sold_currency_ui.addItem("")
        self.sold_currency_ui.setObjectName(u"sold_currency_ui")
        self.sold_currency_ui.setMinimumSize(QSize(95, 0))
        font = QFont()
        font.setPointSize(20)
        self.sold_currency_ui.setFont(font)
        self.sold_currency_ui.setStyleSheet(u"QComboBox {\n"
"   \n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    \n"
"}\n"
"QComboBox QAbstractItemView {\n"
"\n"
"	background-color: rgb(31, 31, 31);\n"
"}\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     \n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"   \n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    \n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    \n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.sold_currency_ui)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.horizontalLayout_5.addWidget(self.sell_frame)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setStyleSheet(u"QFrame{\n"
"background-color: none;\n"
"border:none;\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.sold_creator_royalty = QDoubleSpinBox(self.frame_3)
        self.sold_creator_royalty.setObjectName(u"sold_creator_royalty")
        self.sold_creator_royalty.setStyleSheet(u"font-size: 20pt;")

        self.verticalLayout_3.addWidget(self.sold_creator_royalty)


        self.horizontalLayout_5.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setStyleSheet(u"QFrame{\n"
"background-color: none;\n"
"border:none;\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3)

        self.sold_market_royalty = QDoubleSpinBox(self.frame_2)
        self.sold_market_royalty.setObjectName(u"sold_market_royalty")
        self.sold_market_royalty.setStyleSheet(u"font-size: 20pt;")

        self.verticalLayout_6.addWidget(self.sold_market_royalty)


        self.horizontalLayout_5.addWidget(self.frame_2)


        self.verticalLayout_11.addLayout(self.horizontalLayout_5)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.sell_date_frame = QFrame(self.frame)
        self.sell_date_frame.setObjectName(u"sell_date_frame")
        sizePolicy1.setHeightForWidth(self.sell_date_frame.sizePolicy().hasHeightForWidth())
        self.sell_date_frame.setSizePolicy(sizePolicy1)
        self.sell_date_frame.setStyleSheet(u"QFrame{\n"
"background-color: none;\n"
"border:none;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.sell_date_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.label_5 = QLabel(self.sell_date_frame)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.sold_date_ui = QDateEdit(self.sell_date_frame)
        self.sold_date_ui.setObjectName(u"sold_date_ui")
        self.sold_date_ui.setFont(font)
        self.sold_date_ui.setStyleSheet(u"\n"
"QCalendarWidget QToolButton {\n"
"  font-size: 20pt;\n"
"  }\n"
"/* header row */\n"
"  QCalendarWidget QWidget { alternate-background-color: rgb(128, 128, 128); }\n"
"\n"
"  /* normal days */\n"
"  QCalendarWidget QAbstractItemView:enabled \n"
"  {\n"
"  	font-size:20px;  \n"
"  	color: rgb(255, 255, 255);  \n"
"  	background-color: rgba(255, 255, 255, 30);  \n"
"  	selection-background-color: rgb(64, 64, 64); \n"
"  	selection-color: rgb(0, 255, 0); \n"
"  }\n"
"QCalendarWidget QAbstractItemView:disabled \n"
"{ \n"
"color: rgb(64, 64, 64); \n"
"}")
        self.sold_date_ui.setCalendarPopup(False)

        self.verticalLayout.addWidget(self.sold_date_ui)


        self.verticalLayout_2.addWidget(self.sell_date_frame)


        self.verticalLayout_11.addLayout(self.verticalLayout_2)

        self.sold_dialog_button = QPushButton(self.frame)
        self.sold_dialog_button.setObjectName(u"sold_dialog_button")
        self.sold_dialog_button.setMinimumSize(QSize(0, 50))
        self.sold_dialog_button.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_11.addWidget(self.sold_dialog_button)


        self.horizontalLayout_3.addWidget(self.frame)


        self.retranslateUi(sold_dialog)

        QMetaObject.connectSlotsByName(sold_dialog)
    # setupUi

    def retranslateUi(self, sold_dialog):
        sold_dialog.setWindowTitle(QCoreApplication.translate("sold_dialog", u"Dialog", None))
        self.label_4.setText(QCoreApplication.translate("sold_dialog", u"Sell Price", None))
        self.sold_currency_ui.setItemText(0, QCoreApplication.translate("sold_dialog", u"RUB", None))
        self.sold_currency_ui.setItemText(1, QCoreApplication.translate("sold_dialog", u"USDT", None))
        self.sold_currency_ui.setItemText(2, QCoreApplication.translate("sold_dialog", u"ADA", None))
        self.sold_currency_ui.setItemText(3, QCoreApplication.translate("sold_dialog", u"ETH", None))

        self.label.setText(QCoreApplication.translate("sold_dialog", u"Creator Royalty %", None))
        self.label_3.setText(QCoreApplication.translate("sold_dialog", u"Market Royalty %", None))
        self.label_5.setText(QCoreApplication.translate("sold_dialog", u"Sale Date", None))
        self.sold_dialog_button.setText(QCoreApplication.translate("sold_dialog", u"Sold", None))
    # retranslateUi

