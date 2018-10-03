from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import os.path
import sys
sys.path.append('../')
##BASE_DIR = os.path.dirname(os.path.abspath(__file__))
##db_path = "../../Database/InventoryDatabase.db"
##conn=sqlite3.connect(db_path)

class VerifyCredentials:
    def Verify(Username, Password):
        connection = sqlite3.connect("../../Database/InventoryDatabase.db")
        result = connection.execute("SELECT * FROM Users WHERE USERNAME = ? AND PASSWORD = ?",(Username, Password))
        if( len(result.fetchall()) > 0):
            #dapat dito na ipapakita ang Viewer natin ng Database#
            print("user found")
        else:
            print("memde")
##            self.pushButton.clicked.connect(self.LoginError)

