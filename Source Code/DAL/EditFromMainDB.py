import sqlite3
import os.path
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

sys.path.append('../')
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = "../../Database/InventoryDatabase.db"
conn=sqlite3.connect(db_path)

class Edit2MainDB:
    def Edit2DB(itemName, itemNo):
        connection = sqlite3.connect("../../Database/InventoryDatabase.db")
        result = connection.execute("SELECT * FROM Inventory WHERE Item = ?",(itemName, ))
        if( len(result.fetchall()) > 0):
            sql = '''DELETE FROM Inventory WHERE Item=?'''
            cur=conn.cursor()
            values=((itemName,))
            conn.execute(sql, values)


            
            sql = 'INSERT INTO Inventory (Item, Quantity) VALUES(?,?)'
            cur=conn.cursor()
            values=((itemName,itemNo))
            conn.execute(sql, values)
            conn.commit()
            conn.close()
            subprocess.call(['python','../UI/Quantity_Editsuccess.py']) 
        else:
            subprocess.call(['python','../UI/Quantity_Editfail.py'])


                                    
            





        




