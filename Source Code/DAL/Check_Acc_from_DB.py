from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import os.path
import sys
sys.path.append('../')
from DAL.AccessMainDB import ShowDatabase
from DAL.MainDB import MainDatabase
class DB_access:

    def RevealDatabase(self):
        self.MainDatabase.MainUi
    
    def UserVerify(Username,Password):
        connection = sqlite3.connect("../../Database/InventoryDatabase.db")
        result = connection.execute("SELECT * FROM Users WHERE USERNAME = ? AND PASSWORD = ?",(Username, Password))
        if( len(result.fetchall()) > 0):
            DB_access.RevealDatabase
            
            
            # dapat dito na ipapakita ang Viewer natin ng Database #
        else:
             print("failed")



             







        




          
