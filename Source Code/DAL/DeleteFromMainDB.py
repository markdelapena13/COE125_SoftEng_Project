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

        # user_id nung nag log in na sinave sa file
        f = open("../Shared/LoggedUser.txt", "r")
        loggedUserId = f.read()
        f.close()

        # Count the number of users that the item belongs to
        sql = "SELECT COUNT(ui_user_id), I.item_id FROM User_Item " \
              "INNER JOIN Item I on User_Item.ui_item_id = I.item_id " \
              "WHERE I.item_name = ?"

        result = conn.execute(sql, (itemName,))
        (count, item_id) = result.fetchone()

        print(str(count))

        # 1 or more users have the same item.
        # delete sa specific user lang
        if count >= 1:
            sql = "DELETE FROM User_Item WHERE ui_user_id = ? and ui_item_id = ?"
            cur = conn.cursor()
            conn.execute(sql, (loggedUserId, item_id,))
            conn.commit()

            # pag 1 user lang may-ari nung item na un.
            # dba dinilete na sa taas ung record na may item si user na to
            # ngayon delete naman dito ung record ng Item mismo
            if count == 1:
                sql = "DELETE FROM Item WHERE item_id = ?"
                cur = conn.cursor()
                conn.execute(sql, (item_id,))
                conn.commit()

            subprocess.call(['python','../UI/DeleteComplete.py'])
        else:
             # count < 1. malamang 0, so item doesn't exist
             subprocess.call(['python','../UI/DeleteFailed.py'])





