# from PySide6 import (
#     QtGui,
#     QtCore
# )

# from PySide6.QtCore import (
#     QSize
# )
    
# from PySide6.QtGui import (
#     QAction,
#     QIcon,
# )
    
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
    # QTableView
)    

# from PySide6.QtCore import (
#     Qt
# )

import sqlite3

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
        self.mylist = []
        self.new_list = []
        self.counter=0

        self.tableWidget.setRowCount(self.databaseRecords)
        # self.tableWidget.setColumnCount(8)
        # self.tableWidget.setHorizontalHeaderLabels(["Name", "Hex Code", "Color"])
        # self.tableWidget.setItem(0,0, QTableWidgetItem("Name"))
        for key, item in self.database.items():
            # print("%s=%s" % (key, item))
            # print(f"{key}={item}")
            if not self.counter: 
                l1 = f"{key}={item}"
                self.itemlist = list(item)
                self.itemlist.insert(0,"icon")
                # self.itemlist = list(item)
                self.counter = 1
            self.my_list = list(self.database.keys())
            self.mylist.append(str(key))
            self.new_list = list(set(self.mylist))
            
        # print(f" MyList {self.mylist}")    
        # print(f" NewList {self.my_list}")
        print(f"Item = {self.itemlist}")
        print(f"Length = {len(self.itemlist)}")
        self.itemlist = [i.title() for i in self.itemlist]
        self.tableWidget.setColumnCount(len(self.itemlist))
        self.tableWidget.setHorizontalHeaderLabels(self.itemlist)
        # print(f"L1 = {l1}")

    def setupDatabase(self) -> None:
        self.databaseName = 'projectionist.db'
        self.tablename = "Apps"
        self.database = SqliteDict(
            self.databaseName,
            tablename=self.tablename,
            autocommit=True
        )
        self.databaseRecords = len(self.database)
        
        con = sqlite3.connect("projectionist.db")
        cur = con.cursor()
        res = cur.execute("SELECT key FROM Apps LIMIT 1")
        self.first_row = res.fetchone()
        print(f"First Row is {self.first_row}")
        con.close()
        
        