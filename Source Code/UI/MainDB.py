# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DB_UI.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import sys
import sqlite3
sys.path.append('../')
sys.path.append('../')
db_path = "../../Database/InventoryDatabase.db"
conn = sqlite3.connect(db_path)


class MainDatabase(object):

    sortAscToggle = True

    def __init__(self):
        f = open("../Shared/LoggedUser.txt", "r")
        self.loggedUserId = f.read()
        f.close()

    def MainUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(964, 736)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Add_Item = QtWidgets.QPushButton(self.centralwidget)
        self.Add_Item.setGeometry(QtCore.QRect(50, 170, 93, 28))
        self.Add_Item.setObjectName("Add_Item")

        self.Add_Item.clicked.connect(self.addItem)

        # For loading database
        self.load_data = QtWidgets.QPushButton(self.centralwidget)
        self.load_data.setGeometry(QtCore.QRect(525, 660, 120, 50))
        self.load_data.setObjectName("Load_database")

        self.load_data.clicked.connect(self.loaddata)

        self.Delet_item = QtWidgets.QPushButton(self.centralwidget)
        self.Delet_item.setGeometry(QtCore.QRect(50, 230, 93, 28))
        self.Delet_item.setObjectName("Delet_item")

        self.Delet_item.clicked.connect(self.deleteItem)

        self.DB_Table = QtWidgets.QTableWidget(self.centralwidget)
        self.DB_Table.setGeometry(QtCore.QRect(270, 20, 631, 631))
        self.DB_Table.setObjectName("DB_Table")
        self.DB_Table.setColumnCount(0)
        self.DB_Table.setRowCount(0)

        self.Quit_button = QtWidgets.QPushButton(self.centralwidget)
        self.Quit_button.setGeometry(QtCore.QRect(60, 610, 93, 28))

        self.Quit_button.setObjectName("Quit_button")
        self.Quit_button.clicked.connect(self.close)

        self.Item_Number = QtWidgets.QPushButton(self.centralwidget)
        self.Item_Number.setGeometry(QtCore.QRect(50, 290, 93, 28))
        self.Item_Number.setObjectName("Item_Number")

        self.Item_Number.clicked.connect(self.editItem)

        self.Welcum = QtWidgets.QLabel(self.centralwidget)
        self.Welcum.setGeometry(QtCore.QRect(10, 20, 211, 61))
        self.Welcum.setObjectName("Welcum")
        self.ActionLabel = QtWidgets.QLabel(self.centralwidget)
        self.ActionLabel.setGeometry(QtCore.QRect(10, 140, 101, 16))
        self.ActionLabel.setObjectName("ActionLabel")

        self.item_Sort = QtWidgets.QPushButton(self.centralwidget)
        self.item_Sort.setGeometry(QtCore.QRect(50, 350, 93, 28))
        self.item_Sort.setObjectName("item_Sort")

        self.item_Sort.clicked.connect(self.itemSort)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 964, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Inventory A+"))
        self.Add_Item.setText(_translate("MainWindow", "Add Item"))
        self.load_data.setText(_translate("MainWindow", "Load Data"))
        self.Delet_item.setText(_translate("MainWindow", "Delete Item"))
        self.Quit_button.setText(_translate("MainWindow", "Quit"))
        self.Item_Number.setText(_translate("MainWindow", "Edit Quantity"))
        self.Welcum.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Welcome</span></p></body></html>"))
        self.ActionLabel.setText(_translate("MainWindow", "User Actions:"))
        self.item_Sort.setText(_translate("MainWindow", "Sort Items"))

        # after ng setup ng gui
        # i-load natin ung initial laman nung table
        self.loaddata()

    def loaddata(self):
        rows = self.fetchData()

        # set ung title ng columns. at column count
        self.setupTable()

        # display mo ung rows
        self.displayData(rows)

    def fetchData(self):
        # hiniwalay natin to para testable pag nag add ng item
        sql = "SELECT I.item_name, quantity FROM User_Item INNER JOIN Item I ON ui_item_id = I.item_id WHERE ui_user_id = ?"
        cur = conn.cursor()
        result = cur.execute(sql, (self.loggedUserId,))
        return result.fetchall()


    def setupTable(self):
        colHeaders = ["Item Name", "Quantity"]
        colCount = len(colHeaders)
        self.DB_Table.setColumnCount(colCount)
        self.DB_Table.setHorizontalHeaderLabels(colHeaders)
        self.DB_Table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        for i in range(colCount):
            self.DB_Table.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

    def displayData(self, rows):
        rowCount = len(rows)
        self.DB_Table.setRowCount(rowCount)

        for i in range(rowCount):
            (item_name, quantity) = rows[i]
            tableItemName = QtWidgets.QTableWidgetItem(str(item_name))
            tableItemQuantity = QtWidgets.QTableWidgetItem(str(quantity))
            self.DB_Table.setItem(i, 0, tableItemName)
            self.DB_Table.setItem(i, 1, tableItemQuantity)

    def addItem(self):
        subprocess.call(['python','../UI/Add_item.py'])
        self.loaddata()
    def deleteItem(self):
        subprocess.call(['python','../UI/Delete_item.py'])
        self.loaddata()
    def editItem(self):
        subprocess.call(['python','../UI/Edit_Quantity.py'])
        self.loaddata()

    def itemSort(self):
        self.sortAscToggle = not self.sortAscToggle
        order = ("ASC", "DESC")[self.sortAscToggle == True]
        sql = "SELECT I.item_name, quantity FROM User_Item INNER JOIN Item I ON ui_item_id = I.item_id WHERE ui_user_id = ? ORDER BY item_name " + order

        cur = conn.cursor()
        result = cur.execute(sql, (self.loggedUserId,))
        rows = result.fetchall()

        # set ung title ng columns. at column count
        self.setupTable()

        # display mo ung rows
        self.displayData(rows)


    def close(self):
        sys.exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainDatabase()
    ui.MainUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
