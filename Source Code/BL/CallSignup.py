from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import os.path
import sys
sys.path.append('../')
from DAL.Signup import User_signup
import subprocess

class Write2DB:
    def callUserSignup():
        subprocess.call(['python','../DAL/Signup.py'])


