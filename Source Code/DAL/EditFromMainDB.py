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

        # user_id nung nag log in na sinave sa file
        f = open("../Shared/LoggedUser.txt", "r")
        loggedUserId = f.read()
        f.close()

        # count the number of  times item_name exists for user_id
        # pag count > 0, meaning, the user has this item, else doesn't exists for the logged in user
        sql = "SELECT COUNT(item_id), ui_item_id FROM User_Item " \
              "INNER JOIN Item I on User_Item.ui_item_id = I.item_id " \
              "WHERE ui_user_id = ? AND I.item_name = ?"

        result = conn.execute(sql, (loggedUserId, itemName,))
        (count, item_id) = result.fetchone()

        print(str(count))

        if count > 0 :
            # update na ung quantity for the item of the logged in user
            sql = "UPDATE User_Item SET quantity = ? WHERE ui_user_id = ? and ui_item_id = ?"
            conn.execute(sql, (itemNo, loggedUserId, item_id,))
            conn.commit()
            subprocess.call(['python', '../UI/Quantity_Editsuccess.py'])
        else:
            subprocess.call(['python', '../UI/Quantity_Editfail.py'])

        # result = connection.execute("SELECT * FROM Inventory WHERE Item = ?",(itemName, ))
        # if( len(result.fetchall()) > 0):
        #     sql = '''DELETE FROM Inventory WHERE Item=?'''
        #     cur=conn.cursor()
        #     values=((itemName,))
        #     conn.execute(sql, values)
        #
        #
        #
        #     sql = 'INSERT INTO Inventory (Item, Quantity) VALUES(?,?)'
        #     cur=conn.cursor()
        #     values=((itemName,itemNo))
        #     conn.execute(sql, values)
        #     conn.commit()
        #     conn.close()
        #     subprocess.call(['python','../UI/Quantity_Editsuccess.py'])
        # else:
        #     subprocess.call(['python','../UI/Quantity_Editfail.py'])


                                    
            





        




