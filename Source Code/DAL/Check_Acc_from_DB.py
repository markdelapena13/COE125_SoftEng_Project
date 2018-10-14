from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import os.path
import sys
import subprocess
sys.path.append('../')

class DB_access:
    def UserVerify(Username, Password):
        rows = DB_access.getUserByUserPass(Username, Password)

        if len(rows) > 0:
            # write sa file kung sino ung user na nag log in
            f = open('../Shared/LoggedUser.txt', "w")
            f.write(str(rows[0][0]))
            f.close()

            subprocess.call(['python','../UI/MainDB.py'])
        else:
             subprocess.call(['python','../UI/LoginErr.py'])

    def getUserByUserPass(username, password):
        connection = sqlite3.connect("../../Database/InventoryDatabase.db")
        result = connection.execute("SELECT * FROM User WHERE username = ? AND password = ?", (username, password))
        return result.fetchall()







        




          
