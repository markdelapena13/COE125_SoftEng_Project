from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import os.path
import sys
sys.path.append('../')
from DAL.MainDB import MainDatabase
from DAL.Signup import User_signup

class ShowDatabase:
    
    def AccessDatabase():
        
        MainDatabase.MainUi(self)
