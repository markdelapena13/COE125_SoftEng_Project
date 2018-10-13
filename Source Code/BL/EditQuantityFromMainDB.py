import sqlite3
import os.path
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('../')
from DAL.EditFromMainDB import Edit2MainDB
import subprocess
class MainDBEdit:

    def Edit_Quantity(detail1,detail2):
        name=detail1
        quantity=detail2
        Edit2MainDB.Edit2DB(detail1,detail2)
