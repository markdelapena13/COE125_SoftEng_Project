from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import os.path
import sys
import subprocess
sys.path.append('../')


class DB_access:   
    def UserVerify(Username,Password):
        loginFlag = 0
        connection = sqlite3.connect("../../Database/InventoryDatabase.db")
        result = connection.execute("SELECT * FROM Users WHERE USERNAME = ? AND PASSWORD = ?",(Username, Password))
        if( len(result.fetchall()) > 0):
            subprocess.call(['python','../DAL/MainDB.py'])
            
            
            
            # dapat dito na ipapakita ang Viewer natin ng Database #
        else:
             subprocess.call(['python','../UI/LoginErr.py'])

             





        




          
