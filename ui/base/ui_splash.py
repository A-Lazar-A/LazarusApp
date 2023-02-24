# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_splash.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QProgressBar, QSizePolicy, QVBoxLayout, QWidget)

class Ui_SplashWindow(object):
    def setupUi(self, SplashWindow):
        if not SplashWindow.objectName():
            SplashWindow.setObjectName(u"SplashWindow")
        SplashWindow.resize(800, 500)
        SplashWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(SplashWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(31, 31, 31);\n"
"color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 120, 771, 71))
        font = QFont(":/fonts/Ubuntu-R.ttf")
        font.setPointSize(40)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(40, 320, 701, 31))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	background-color: rgb(57, 57, 57);\n"
"text-align: center;\n"
"border-radius: 15px;\n"
"border-style: none;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	background-color: qlineargradient(spread:pad, x1:0.00497512, y1:0.557, x2:1, y2:0.568, stop:0 rgba(39, 39, 39, 255), stop:1 rgba(94, 92, 100, 255));\n"
"border-radius: 15px;\n"
"}")
        self.progressBar.setValue(24)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 450, 741, 21))
        font1 = QFont(":/fonts/Ubuntu-R.ttf")
        font1.setPointSize(12)
        font1.setBold(False)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.frame)

        SplashWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashWindow)

        QMetaObject.connectSlotsByName(SplashWindow)
    # setupUi

    def retranslateUi(self, SplashWindow):
        SplashWindow.setWindowTitle(QCoreApplication.translate("SplashWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("SplashWindow", u"<strong>Lazarus</strong>App", None))
        self.label_2.setText(QCoreApplication.translate("SplashWindow", u"<html><head/><body><p>Created by @A_Lazar_A</p></body></html>", None))
    # retranslateUi

