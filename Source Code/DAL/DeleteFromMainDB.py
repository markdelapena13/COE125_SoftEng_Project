import sqlite3
import os.path
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

sys.path.append('../')
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = "../../Database/InventoryDatabase.db"
conn=sqlite3.connect(db_path)

class Delete2MainDB:
    def Delete2DB(itemName):
        connection = sqlite3.connect("../../Database/InventoryDatabase.db")
        result = connection.execute("SELECT * FROM Inventory WHERE item = ?",(itemName, ))
        if( len(result.fetchall()) > 0):
            sql = '''DELETE FROM Inventory WHERE Item=?'''
            cur=conn.cursor()
            values=((itemName,))
            conn.execute(sql, values)
            conn.commit()
            conn.close()
            subprocess.call(['python','../UI/DeleteComplete.py']) 
                                    
            
        else:
             subprocess.call(['python','../UI/DeleteFailed.py'])




        
##        sql = '''DELETE FROM Inventory WHERE Item=?'''
##        cur=conn.cursor()
##        values=((itemName,))
##        conn.execute(sql, values)
##        conn.commit()
##        conn.close()




