from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import os.path
import sys
sys.path.append('../')
from DAL.Check_Acc_from_DB import DB_access
from DAL.Signup import User_signup

class VerifyCredentials:
    #this class is for checking the database#
    def AskDatabase(Username1, Password1):
        Username=Username1
        Password=Password1
        DB_access.UserVerify(Username,Password)


class Write2DB:
    #this class is for writing to the Users table in the Database#
    def register():
        Signup.User_signup
    
        

