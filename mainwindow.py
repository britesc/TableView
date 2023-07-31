import os

from PySide6 import (
    QtGui,
    QtCore
)

from PySide6.QtCore import (
    QSize,
    QFileInfo
)
    
from PySide6.QtGui import (
    QAction,
    QIcon,
    QPixmap
)
    
from PySide6.QtWidgets import (
    QMainWindow,
    # QToolBar,
    # QPushButton,
    # QStatusBar,
    # QApplication,
    QHeaderView,
    # QAbstractItemView,
    QTableWidget,
    QTableWidgetItem,
    # QVBoxLayout,
    # QHBoxLayout,
    # QTableView,
    QLabel,
)    

from PySide6.QtCore import (
    Qt
)

from sqlitedict import (
    SqliteDict
)

from mainwindow_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app) -> None:
        super().__init__()
        self.setupUi(self) # type: ignore
        self.app = app #declare an app member

        self.setupDatabase()

        self.table_widget = QTableWidget()
        # self.mylist = []
        # self.new_list = []
        self.counter=0
        self.keylist = []

        self.tableWidget.setRowCount(self.databaseRecords)

        self.makeHeader()
        self.populateTable()
        
        self.vAppReal = ""
        self.vAppAlias = ""
        self.vLocation = ""
        self.vVersion = ""
        self.vType = ""                
                        
        self.pushButton1_New.clicked.connect(self._rowAdd)  # type: ignore
        self.pushButton2_Save.clicked.connect(self._rowSave)  # type: ignore
        self.pushButton3_Delete.clicked.connect(self._rowDelete)  # type: ignore
        self.tableWidget.cellClicked.connect(self._rowSelected) # type: ignore
        
        self.pushButton2_Save.setEnabled(False)
        self.pushButton3_Delete.setEnabled(False)


    def setupDatabase(self) -> None:
        self.databaseName = 'projectionist.db'
        self.tablename = "Apps"
        self.database = SqliteDict(
            self.databaseName,
            tablename=self.tablename,
            autocommit=True
        )
        self.databaseRecords = len(self.database)
        
    def makeHeader(self) -> None:
        headerCounter = 0
        for key, item in self.database.items():
            if not headerCounter: 
                self.keylist = list(item)
                self.keylist.insert(0,"icon")
                headerCounter = 1

        self.keylist = [i.title() for i in self.keylist]
        self.tableWidget.setColumnCount(len(self.keylist))
        self.tableWidget.setHorizontalHeaderLabels(self.keylist)  
        
        self.tableWidget.horizontalHeader().resizeSection(0, 16)
        self.tableWidget.horizontalHeader().resizeSection(1, 250)
        self.tableWidget.horizontalHeader().resizeSection(2, 250)
        self.tableWidget.horizontalHeader().resizeSection(4, 150)
        self.tableWidget.horizontalHeader().resizeSection(5, 150)
            
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)   # noqa: E501 # icon
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Interactive)   # noqa: E501 # app
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Interactive)   # noqa: E501 # alias
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)   # noqa: E501 # location
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeMode.Interactive)   # noqa: E501 # version
        self.tableWidget.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeMode.Stretch)   # noqa: E501 # type
        
    def populateTable(self) -> None:     # sourcery skip: use-named-expression
        rowCounter = 0
        valueList = []
        icon_location = "/home/julian/Downloads/logos/Dones/"

        for key, item in self.database.items():

            valueList = list(item.values())

            self.tableWidget.setItem(rowCounter,1, QTableWidgetItem(valueList[0]))
            self.tableWidget.setItem(rowCounter,2, QTableWidgetItem(valueList[1]))
            self.tableWidget.setItem(rowCounter,3, QTableWidgetItem(valueList[2]))
            self.tableWidget.setItem(rowCounter,4, QTableWidgetItem(valueList[3]))
            self.tableWidget.setItem(rowCounter,5, QTableWidgetItem(valueList[4]))
            self.tableWidget.setSortingEnabled(True)
            
            icon_size = QSize(36,36)
            icon_label = QLabel()
            icon_label.setMaximumSize(icon_size)
            icon_label.resize(icon_size)
                        
            icon_to_test = f"{icon_location}{valueList[0]}.png"
            
            if os.path.isfile(icon_to_test):
                make_icon = f"{icon_location}{valueList[0]}.png"
            else:
                make_icon = f"{icon_location}notfound.png"
                    
            icon_pixmap = QPixmap(make_icon)
        
            icon_pixmap = icon_pixmap.scaled(36,36, Qt.KeepAspectRatio)  # type: ignore
            icon_label.setPixmap(icon_pixmap)
            icon_label.setScaledContents(True)
            icon_label.resize(icon_size)
            self.tableWidget.setCellWidget(rowCounter,0, icon_label)
            rowCounter = rowCounter + 1
            
    def _rowAdd(self) -> None:
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        self.pushButton2_Save.setEnabled(True)
        
    def _rowDelete(self) -> None:
        rowPosition = self.tableWidget.currentRow()
        print(f"Deleting Row {rowPosition}")
        self.tableWidget.removeRow(rowPosition)
        self.database.pop(f"{self.vAppReal}")
        
        
        self.tableWidget.selectRow(rowPosition)
        
    
    def _rowSave(self) -> None:  # sourcery skip: class-extract-method
        # rowPosition = self.tableWidget.currentRow()
        self.pushButton2_Save.setEnabled(False)
        # print(f"Saving Row {rowPosition}")
        # print(f"self.vAppReal = {self.vAppReal}")
        # print(f"self.vAppAlias = {self.vAppAlias}")
        # print(f"self.vLocation = {self.vLocation}")
        # print(f"self.vVersion = {self.vVersion}")
        # print(f"self.vType = {self.vType}")
                
        self.database[f"{self.vAppReal}"] = {
            'app': self.vAppReal,
            'alias': self.vAppAlias,
            'location': self.vLocation,
            'version': self.vVersion,
            'type': self.vType
            }
        self.database.commit()  # type: ignore 
    
    def _rowSelected(self) -> None:
        self.pushButton3_Delete.setEnabled(True)
        rowPosition = self.tableWidget.currentRow()
        # print(f"Selected Row {rowPosition}")

        if self.tableWidget.item(rowPosition, 1):
            self.vAppReal = self.tableWidget.item(rowPosition, 1).text()
        if self.tableWidget.item(rowPosition, 2):
            self.vAppAlias = self.tableWidget.item(rowPosition, 2).text()
        if self.tableWidget.item(rowPosition, 3):
            self.vLocation = self.tableWidget.item(rowPosition, 3).text()
        if self.tableWidget.item(rowPosition, 4):
            self.vVersion = self.tableWidget.item(rowPosition, 4).text()
        if self.tableWidget.item(rowPosition, 5):
            self.vType = self.tableWidget.item(rowPosition, 5).text()

        # print(f"self.vAppReal = {self.vAppReal}")
        # print(f"self.vAppAlias = {self.vAppAlias}")
        # print(f"self.vLocation = {self.vLocation}")
        # print(f"self.vVersion = {self.vVersion}")
        # print(f"self.vType = {self.vType}")
