from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import os.path
import sys
sys.path.append('../')


class DB_access:
    def UserVerify(Username,Password):
        connection = sqlite3.connect("../../Database/InventoryDatabase.db")
        result = connection.execute("SELECT * FROM Users WHERE USERNAME = ? AND PASSWORD = ?",(Username, Password))
        if( len(result.fetchall()) > 0):
            #dapat dito na ipapakita ang Viewer natin ng Database#
            print("user found")
        else:
            print("memde")
##            self.pushButton.clicked.connect(self.LoginError)
