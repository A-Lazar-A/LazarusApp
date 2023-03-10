# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialog.ui'
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
                               QLabel, QLineEdit, QPushButton, QSizePolicy,
                               QSpinBox, QVBoxLayout, QWidget)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(744, 321)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(744, 0))
        Dialog.setStyleSheet(u"background-color: rgb(31, 31, 31);\n"
                             "color: rgb(255, 255, 255);")
        self.horizontalLayout_2 = QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
                                 "border: 1px solid rgba(255, 255, 255, 40);\n"
                                 "border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.item_name = QLineEdit(self.frame)
        self.item_name.setObjectName(u"item_name")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.item_name.sizePolicy().hasHeightForWidth())
        self.item_name.setSizePolicy(sizePolicy2)
        id = QFontDatabase.addApplicationFont(":/fonts/Roboto-Regular.ttf")
        family = QFontDatabase.applicationFontFamilies(id)[0]

        font = QFont(family)
        font.setPointSize(20)
        self.item_name.setFont(font)
        self.item_name.setStyleSheet(u"margin-top:18px;")

        self.horizontalLayout_4.addWidget(self.item_name)

        self.purch_date_frame = QFrame(self.frame)
        self.purch_date_frame.setObjectName(u"purch_date_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.purch_date_frame.sizePolicy().hasHeightForWidth())
        self.purch_date_frame.setSizePolicy(sizePolicy3)
        self.purch_date_frame.setStyleSheet(u"QFrame{\n"
                                            "background-color: none;\n"
                                            "border:none;\n"
                                            "}\n"
                                            "")
        self.verticalLayout = QVBoxLayout(self.purch_date_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.purch_date_frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))
        font1 = QFont(family)
        font1.setFamilies([u"Ubuntu"])
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: none;\n"
                                 "border: none;\n"
                                 "")
        self.label.setMargin(0)

        self.verticalLayout.addWidget(self.label)

        self.buy_date_ui = QDateEdit(self.purch_date_frame)
        self.buy_date_ui.setObjectName(u"buy_date_ui")
        self.buy_date_ui.setFont(font)
        self.buy_date_ui.setStyleSheet(u"\n"
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
        self.buy_date_ui.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.buy_date_ui.setCalendarPopup(False)

        self.verticalLayout.addWidget(self.buy_date_ui)

        self.horizontalLayout_4.addWidget(self.purch_date_frame)

        self.sell_date_frame = QFrame(self.frame)
        self.sell_date_frame.setObjectName(u"sell_date_frame")
        sizePolicy3.setHeightForWidth(self.sell_date_frame.sizePolicy().hasHeightForWidth())
        self.sell_date_frame.setSizePolicy(sizePolicy3)
        self.sell_date_frame.setStyleSheet(u"QFrame{\n"
                                           "background-color: none;\n"
                                           "border:none;\n"
                                           "}\n"
                                           "")
        self.verticalLayout_2 = QVBoxLayout(self.sell_date_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.label_2 = QLabel(self.sell_date_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 20))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: none;\n"
                                   "border: none;\n"
                                   "margin-left: 2px;")

        self.verticalLayout_2.addWidget(self.label_2)

        self.sell_date_ui = QDateEdit(self.sell_date_frame)
        self.sell_date_ui.setObjectName(u"sell_date_ui")
        self.sell_date_ui.setFont(font)
        self.sell_date_ui.setStyleSheet(u"\n"
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
        self.sell_date_ui.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sell_date_ui.setCalendarPopup(False)

        self.verticalLayout_2.addWidget(self.sell_date_ui)

        self.horizontalLayout_4.addWidget(self.sell_date_frame)

        self.verticalLayout_11.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.price_frame = QFrame(self.frame)
        self.price_frame.setObjectName(u"price_frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.price_frame.sizePolicy().hasHeightForWidth())
        self.price_frame.setSizePolicy(sizePolicy4)
        self.price_frame.setMinimumSize(QSize(211, 0))
        self.price_frame.setStyleSheet(u"QFrame{\n"
                                       "background-color: none;\n"
                                       "border:none;\n"
                                       "}\n"
                                       "")
        self.verticalLayout_3 = QVBoxLayout(self.price_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.label_3 = QLabel(self.price_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 20))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background-color: none;\n"
                                   "border: none;")

        self.verticalLayout_3.addWidget(self.label_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.buy_price_ui = QDoubleSpinBox(self.price_frame)
        self.buy_price_ui.setObjectName(u"buy_price_ui")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.buy_price_ui.sizePolicy().hasHeightForWidth())
        self.buy_price_ui.setSizePolicy(sizePolicy5)
        self.buy_price_ui.setMinimumSize(QSize(90, 0))
        self.buy_price_ui.setFont(font)
        self.buy_price_ui.setStyleSheet(u"font-size: 20pt;\n"
                                        "")
        self.buy_price_ui.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.buy_price_ui.setDecimals(4)
        self.buy_price_ui.setMaximum(99999999999999991611392.000000000000000)
        self.buy_price_ui.setStepType(QAbstractSpinBox.DefaultStepType)

        self.horizontalLayout_3.addWidget(self.buy_price_ui)

        self.buy_currency_ui = QComboBox(self.price_frame)
        self.buy_currency_ui.addItem("")
        self.buy_currency_ui.addItem("")
        self.buy_currency_ui.addItem("")
        self.buy_currency_ui.addItem("")
        self.buy_currency_ui.setObjectName(u"buy_currency_ui")
        sizePolicy5.setHeightForWidth(self.buy_currency_ui.sizePolicy().hasHeightForWidth())
        self.buy_currency_ui.setSizePolicy(sizePolicy5)
        self.buy_currency_ui.setMinimumSize(QSize(95, 0))
        self.buy_currency_ui.setFont(font)
        self.buy_currency_ui.setStyleSheet(u"QComboBox {\n"
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

        self.horizontalLayout_3.addWidget(self.buy_currency_ui)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5.addWidget(self.price_frame)

        self.sell_frame = QFrame(self.frame)
        self.sell_frame.setObjectName(u"sell_frame")
        sizePolicy4.setHeightForWidth(self.sell_frame.sizePolicy().hasHeightForWidth())
        self.sell_frame.setSizePolicy(sizePolicy4)
        self.sell_frame.setMinimumSize(QSize(211, 0))
        self.sell_frame.setStyleSheet(u"QFrame{\n"
                                      "background-color: none;\n"
                                      "border:none;\n"
                                      "}\n"
                                      "")
        self.verticalLayout_4 = QVBoxLayout(self.sell_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.sell_frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy6)
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"background-color: none;\n"
                                   "border: none;")

        self.verticalLayout_4.addWidget(self.label_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sell_price_ui = QDoubleSpinBox(self.sell_frame)
        self.sell_price_ui.setObjectName(u"sell_price_ui")
        sizePolicy5.setHeightForWidth(self.sell_price_ui.sizePolicy().hasHeightForWidth())
        self.sell_price_ui.setSizePolicy(sizePolicy5)
        self.sell_price_ui.setMinimumSize(QSize(90, 0))
        self.sell_price_ui.setFont(font)
        self.sell_price_ui.setStyleSheet(u"font-size: 20pt;\n"
                                         "")
        self.sell_price_ui.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sell_price_ui.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.sell_price_ui.setDecimals(4)
        self.sell_price_ui.setMaximum(99999999999999991611392.000000000000000)
        self.sell_price_ui.setStepType(QAbstractSpinBox.DefaultStepType)

        self.horizontalLayout.addWidget(self.sell_price_ui)

        self.sell_currency_ui = QComboBox(self.sell_frame)
        self.sell_currency_ui.addItem("")
        self.sell_currency_ui.addItem("")
        self.sell_currency_ui.addItem("")
        self.sell_currency_ui.addItem("")
        self.sell_currency_ui.setObjectName(u"sell_currency_ui")
        sizePolicy5.setHeightForWidth(self.sell_currency_ui.sizePolicy().hasHeightForWidth())
        self.sell_currency_ui.setSizePolicy(sizePolicy5)
        self.sell_currency_ui.setMinimumSize(QSize(95, 0))
        self.sell_currency_ui.setFont(font)
        self.sell_currency_ui.setStyleSheet(u"QComboBox {\n"
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

        self.horizontalLayout.addWidget(self.sell_currency_ui)

        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_5.addWidget(self.sell_frame)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy4.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy4)
        self.frame_2.setStyleSheet(u"QFrame{\n"
                                   "background-color: none;\n"
                                   "border:none;\n"
                                   "}\n"
                                   "")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy7)
        self.label_6.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_6)

        self.creator_royalty_ui = QDoubleSpinBox(self.frame_2)
        self.creator_royalty_ui.setObjectName(u"creator_royalty_ui")
        sizePolicy5.setHeightForWidth(self.creator_royalty_ui.sizePolicy().hasHeightForWidth())
        self.creator_royalty_ui.setSizePolicy(sizePolicy5)
        self.creator_royalty_ui.setFont(font)
        self.creator_royalty_ui.setStyleSheet(u"font-size: 20pt;")
        self.creator_royalty_ui.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.creator_royalty_ui.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.verticalLayout_6.addWidget(self.creator_royalty_ui)

        self.horizontalLayout_5.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy4.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy4)
        self.frame_3.setLayoutDirection(Qt.LeftToRight)
        self.frame_3.setStyleSheet(u"QFrame{\n"
                                   "background-color: none;\n"
                                   "border:none;\n"
                                   "}\n"
                                   "")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, 0, -1)
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        sizePolicy7.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy7)
        self.label_7.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_7)

        self.market_royalty_ui = QDoubleSpinBox(self.frame_3)
        self.market_royalty_ui.setObjectName(u"market_royalty_ui")
        sizePolicy5.setHeightForWidth(self.market_royalty_ui.sizePolicy().hasHeightForWidth())
        self.market_royalty_ui.setSizePolicy(sizePolicy5)
        self.market_royalty_ui.setFont(font)
        self.market_royalty_ui.setStyleSheet(u"font-size: 20pt;")
        self.market_royalty_ui.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.market_royalty_ui.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.verticalLayout_7.addWidget(self.market_royalty_ui)

        self.horizontalLayout_5.addWidget(self.frame_3)

        self.verticalLayout_11.addLayout(self.horizontalLayout_5)

        self.q_frame = QFrame(self.frame)
        self.q_frame.setObjectName(u"q_frame")
        sizePolicy3.setHeightForWidth(self.q_frame.sizePolicy().hasHeightForWidth())
        self.q_frame.setSizePolicy(sizePolicy3)
        self.q_frame.setStyleSheet(u"QFrame{\n"
                                   "background-color: none;\n"
                                   "border:none;\n"
                                   "}\n"
                                   "")
        self.verticalLayout_5 = QVBoxLayout(self.q_frame)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(1, 1, 1, 1)
        self.label_5 = QLabel(self.q_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 20))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"background-color: none;\n"
                                   "border: none;\n"
                                   "")

        self.verticalLayout_5.addWidget(self.label_5)

        self.quantity_ui = QSpinBox(self.q_frame)
        self.quantity_ui.setObjectName(u"quantity_ui")
        self.quantity_ui.setFont(font)
        self.quantity_ui.setStyleSheet(u"font-size: 20pt;\n"
                                       "")
        self.quantity_ui.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.quantity_ui.setMinimum(1)

        self.verticalLayout_5.addWidget(self.quantity_ui)

        self.verticalLayout_11.addWidget(self.q_frame)

        self.add_dialog_button = QPushButton(self.frame)
        self.add_dialog_button.setObjectName(u"add_dialog_button")
        self.add_dialog_button.setMinimumSize(QSize(0, 50))
        self.add_dialog_button.setFont(font1)
        self.add_dialog_button.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_11.addWidget(self.add_dialog_button)

        self.horizontalLayout_2.addWidget(self.frame)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.item_name.setText(QCoreApplication.translate("Dialog", u"Item Name", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Purchace Date", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Sell Date", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Price", None))
        self.buy_currency_ui.setItemText(0, QCoreApplication.translate("Dialog", u"RUB", None))
        self.buy_currency_ui.setItemText(1, QCoreApplication.translate("Dialog", u"USDT", None))
        self.buy_currency_ui.setItemText(2, QCoreApplication.translate("Dialog", u"ADA", None))
        self.buy_currency_ui.setItemText(3, QCoreApplication.translate("Dialog", u"ETH", None))

        self.label_4.setText(QCoreApplication.translate("Dialog", u"Sell Price", None))
        self.sell_currency_ui.setItemText(0, QCoreApplication.translate("Dialog", u"RUB", None))
        self.sell_currency_ui.setItemText(1, QCoreApplication.translate("Dialog", u"USDT", None))
        self.sell_currency_ui.setItemText(2, QCoreApplication.translate("Dialog", u"ADA", None))
        self.sell_currency_ui.setItemText(3, QCoreApplication.translate("Dialog", u"ETH", None))

        self.label_6.setText(QCoreApplication.translate("Dialog", u"Creator Royalty %", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Market Royalty %", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Quantity", None))
        self.add_dialog_button.setText(QCoreApplication.translate("Dialog", u"Add", None))
    # retranslateUi
