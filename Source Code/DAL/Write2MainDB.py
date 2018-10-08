import sqlite3
import os.path
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

sys.path.append('../')


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = "../../Database/InventoryDatabase.db"
conn=sqlite3.connect(db_path)

class Add2MainDB:
    def Write2DB(itemName,itemNo):  
        sql='INSERT INTO Inventory(Item,Quantity) VALUES(?,?)'
        cur=conn.cursor()
        values=(itemName,itemNo)
        conn.execute(sql, values)
        conn.commit()
        conn.close()

