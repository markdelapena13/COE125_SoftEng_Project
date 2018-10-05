import sqlite3
import os.path
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('../')
from DAL.Write2MainDB import Add2MainDB
import subprocess


class MainDBWrite:


    def Add_Items(detail1,detail2):
        name=detail1
        quantity=detail2
        Add2MainDB.Write2DB(detail1,detail2)
##        subprocess.call(['python','../DAL/Write2MainDB.py'])
