from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import os.path
import sys
sys.path.append('../')
from DAL.Check_Acc_from_DB import DB_access
from DAL.Signup import User_signup

class VerifyCredentials:
    
    def AskDatabase(Username1, Password1):
        Var1=Username1
        Var2=Password1
        DB_access.UserVerify(Var1,Var2)


class Write2DB:
    def register():
        Signup.User_signup


