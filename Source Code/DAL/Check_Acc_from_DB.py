from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import os.path
import sys
import subprocess
sys.path.append('../')


class DB_access:   
    def UserVerify(Username,Password):
        connection = sqlite3.connect("../../Database/InventoryDatabase.db")
        result = connection.execute("SELECT * FROM Users WHERE USERNAME = ? AND PASSWORD = ?",(Username, Password))
        if( len(result.fetchall()) > 0):
            subprocess.call(['python','../UI/MainDB.py'])
            
        else:
             subprocess.call(['python','../UI/LoginErr.py'])

             





        




          
