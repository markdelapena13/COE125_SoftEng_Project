import sqlite3
import os.path
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

sys.path.append('../')


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = "../../Database/InventoryDatabase.db"
conn=sqlite3.connect(db_path)
cur=conn.cursor()

class display2MainDB:
    def display2DB(itemName,itemNo):
        self.db = Database()
        self.model = Model(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.showColumn(2)
 
        for n in range(45764):
            n=n+10
            self.ui.tableView.setRowHidden(n, True)
      ##  execute ('SELECT * FROM Inventory')
    ##meme = cur.fetchall()
    ##row = len(obj)
        
   ## i=0
    ##while i<row_count:
      ##      print meme[i][0],' '*(12-meme(obj[i][1])),' '(*12-len(meme[i][1], obj[i][2]))
        ##    i=i=1

       ## sql='''INSERT INTO Inventory(Item,Quantity) VALUES(?,?)'''
        ##cur=conn.cursor()
        ##values=(itemName,itemNo)
        ##cur.execute(sql, values)
        ##conn.commit()
        ##conn.close()
        ##print("meme")
