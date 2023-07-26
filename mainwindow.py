from PySide6 import (
    QtGui,
    QtCore
)

from PySide6.QtCore import (
    QSize
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
    # QHeaderView,
    # QAbstractItemView,
    QTableWidget,
    QTableWidgetItem,
    # QVBoxLayout,
    # QHBoxLayout,
    # QTableView,
    QLabel
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
        # self.tableWidget.setColumnCount(8)
        # self.tableWidget.setHorizontalHeaderLabels(["Name", "Hex Code", "Color"])
        self.makeHeader()
        self.populateTable()
        # self.tableWidget.setItem(0,0, QTableWidgetItem("Name"))
        # for key, item in self.database.items():
        #     # print("%s=%s" % (key, item))
        #     # print(f"{key}={item}")
        #     self.tableWidget.setItem(self.counter,0, QTableWidgetItem("Name"))
        #     if not self.counter: 
        #         self.keylist = list(item)
        #         self.keylist.insert(0,"icon")
        #         # self.keylist = list(item)
                
        #     self.counter += 1
                
                
            # self.my_list = list(self.database.keys())
            # self.mylist.append(str(key))
            # self.new_list = list(set(self.mylist))
            
        # print(f" MyList {self.mylist}")    
        # print(f" NewList {self.my_list}")
        # print(f"Item = {self.keylist}")
        # print(f"Length = {len(self.keylist)}")
        # self.keylist = [i.title() for i in self.keylist]
        # self.tableWidget.setColumnCount(len(self.keylist))
        # self.tableWidget.setHorizontalHeaderLabels(self.keylist)

    def setupDatabase(self) -> None:
        self.databaseName = 'projectionist.db'
        self.tablename = "Apps"
        self.database = SqliteDict(
            self.databaseName,
            tablename=self.tablename,
            autocommit=True
        )
        self.databaseRecords = len(self.database)
        
        # con = sqlite3.connect("projectionist.db")
        # cur = con.cursor()
        # res = cur.execute("SELECT key FROM Apps LIMIT 1")
        # self.first_row = res.fetchone()
        # print(f"First Row is {self.first_row}")
        # con.close()
        
    def makeHeader(self) -> None:
        headerCounter = 0
        # valueList =[]
        for key, item in self.database.items():
            # print("%s=%s" % (key, item))
            # print(f"{key}={item}")
            if not headerCounter: 
                self.keylist = list(item)
                self.keylist.insert(0,"icon")
                # self.keylist = list(item)
                headerCounter = 1
        self.keylist = [i.title() for i in self.keylist]
        self.tableWidget.setColumnCount(len(self.keylist))
        self.tableWidget.setHorizontalHeaderLabels(self.keylist)     
        
    def populateTable(self) -> None:   
        rowCounter = 0
        valueList = []
        for key, item in self.database.items():
            #self.tableWidget.setItem(columnCounter,0, QTableWidgetItem(key))
            # print(f"{key}={item}")
            valueList = list(item.values())
            # print(valueList[0])
            self.tableWidget.setItem(rowCounter,1, QTableWidgetItem(valueList[0]))
            self.tableWidget.setItem(rowCounter,2, QTableWidgetItem(valueList[1]))
            self.tableWidget.setItem(rowCounter,3, QTableWidgetItem(valueList[2]))
            self.tableWidget.setItem(rowCounter,4, QTableWidgetItem(valueList[3]))
            self.tableWidget.setItem(rowCounter,5, QTableWidgetItem(valueList[4]))
            
            icon_size = QSize(24,24)
            icon_label = QLabel()
            icon_label.setMaximumSize(icon_size)
            icon_label.resize(icon_size)
            icon_pixmap = QPixmap("about.png")
            icon_pixmap = icon_pixmap.scaled(24,24, Qt.KeepAspectRatio)
            icon_label.setPixmap(icon_pixmap)
            icon_label.setScaledContents(True)
            icon_label.resize(icon_size)
            self.tableWidget.setCellWidget(rowCounter,0, icon_label)

            
            
            
            rowCounter = rowCounter + 1