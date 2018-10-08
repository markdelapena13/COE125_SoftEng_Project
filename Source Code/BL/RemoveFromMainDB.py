import sqlite3
import os.path
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('../')
from DAL.DeleteFromMainDB import Delete2MainDB
import subprocess
class MainDBDelete:

    def Delete_Items(detail1):
        name=detail1
        Delete2MainDB.Delete2DB(detail1)
