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

        # user_id nung nag log in na sinave sa file
        f = open("../Shared/LoggedUser.txt", "r")
        loggedUserId = f.read()
        f.close()
        # print(str(loggedUserId))

        # insert sa item table. pag existing, ignore
        sql = "INSERT OR IGNORE INTO Item(item_name) VALUES (?)"
        cur = conn.cursor()
        cur.execute(sql, (itemName,))
        conn.commit()

        # pag wala pa, maglalagay ng default na 0 quantity. pag existing, ignore lng
        sql = "INSERT OR IGNORE INTO User_Item(ui_user_id, ui_item_id) VALUES(?, (SELECT item_id from Item WHERE item_name = ?))"
        cur = conn.cursor()
        cur.execute(sql, (loggedUserId, itemName,))
        conn.commit()

        # get item id and quantity
        sql = "SELECT item_id, UI.quantity FROM Item INNER JOIN User_Item UI on Item.item_id = UI.ui_item_id WHERE item_name = ? and UI.ui_user_id = ?"
        result = conn.execute(sql, (itemName,loggedUserId,))
        (item_id, quantity) = result.fetchone()
        # print(str((item_id, quantity)))

        # increase the quantity
        quantity = int(quantity) + int(itemNo)

        # pag wala pa, insert. pag meron na, replace na
        sql = "INSERT OR REPLACE INTO User_Item(ui_user_id, ui_item_id, quantity) VALUES(?,?,?)"
        cur = conn.cursor()
        cur.execute(sql, (loggedUserId, item_id, quantity))
        conn.commit()

        conn.close()
