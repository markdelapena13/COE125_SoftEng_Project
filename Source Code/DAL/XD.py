from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import os.path
import sys
sys.path.append('../')
from DAL.Meme import MainDatabase


class ShowDatabase:


    def AccessDatabase():
        MainWindow = QtWidgets.QMainWindow()
        ui = MainDatabase()
        ui.setupUi(MainWindow)
        MainWindow.show()

