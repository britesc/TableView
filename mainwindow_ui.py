# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        font = QFont()
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton3_Delete = QPushButton(self.centralwidget)
        self.pushButton3_Delete.setObjectName(u"pushButton3_Delete")

        self.gridLayout_2.addWidget(self.pushButton3_Delete, 0, 2, 1, 1)

        self.pushButton1_New = QPushButton(self.centralwidget)
        self.pushButton1_New.setObjectName(u"pushButton1_New")

        self.gridLayout_2.addWidget(self.pushButton1_New, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 4, 1, 1)

        self.pushButton2_Save = QPushButton(self.centralwidget)
        self.pushButton2_Save.setObjectName(u"pushButton2_Save")

        self.gridLayout_2.addWidget(self.pushButton2_Save, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Table View of Tools", None))
        self.pushButton3_Delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButton1_New.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.pushButton2_Save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

