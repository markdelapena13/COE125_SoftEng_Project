# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DB_UI.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class MainDatabase(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(964, 736)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Add_Item = QtWidgets.QPushButton(self.centralwidget)
        self.Add_Item.setGeometry(QtCore.QRect(50, 170, 93, 28))
        self.Add_Item.setObjectName("Add_Item")
        self.Delet_item = QtWidgets.QPushButton(self.centralwidget)
        self.Delet_item.setGeometry(QtCore.QRect(50, 230, 93, 28))
        self.Delet_item.setObjectName("Delet_item")
        self.DB_Table = QtWidgets.QTableWidget(self.centralwidget)
        self.DB_Table.setGeometry(QtCore.QRect(270, 20, 631, 631))
        self.DB_Table.setObjectName("DB_Table")
        self.DB_Table.setColumnCount(0)
        self.DB_Table.setRowCount(0)
        self.Quit_button = QtWidgets.QPushButton(self.centralwidget)
        self.Quit_button.setGeometry(QtCore.QRect(60, 610, 93, 28))
        self.Quit_button.setObjectName("Quit_button")
        self.Item_Number = QtWidgets.QPushButton(self.centralwidget)
        self.Item_Number.setGeometry(QtCore.QRect(50, 290, 93, 28))
        self.Item_Number.setObjectName("Item_Number")
        self.User_Field = QtWidgets.QLabel(self.centralwidget)
        self.User_Field.setGeometry(QtCore.QRect(10, 50, 221, 31))
        self.User_Field.setObjectName("User_Field")
        self.Welcum = QtWidgets.QLabel(self.centralwidget)
        self.Welcum.setGeometry(QtCore.QRect(10, 20, 101, 21))
        self.Welcum.setObjectName("Welcum")
        self.ActionLabel = QtWidgets.QLabel(self.centralwidget)
        self.ActionLabel.setGeometry(QtCore.QRect(10, 140, 101, 16))
        self.ActionLabel.setObjectName("ActionLabel")
        self.item_Sort = QtWidgets.QPushButton(self.centralwidget)
        self.item_Sort.setGeometry(QtCore.QRect(50, 350, 93, 28))
        self.item_Sort.setObjectName("item_Sort")
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
        self.Delet_item.setText(_translate("MainWindow", "Delete Item"))
        self.Quit_button.setText(_translate("MainWindow", "Quit"))
        self.Item_Number.setText(_translate("MainWindow", "Select Quantity"))
        self.User_Field.setText(_translate("MainWindow", "Username Appears here"))
        self.Welcum.setText(_translate("MainWindow", "Welcome:"))
        self.ActionLabel.setText(_translate("MainWindow", "User Actions:"))
        self.item_Sort.setText(_translate("MainWindow", "Sort Items"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainDatabase()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

