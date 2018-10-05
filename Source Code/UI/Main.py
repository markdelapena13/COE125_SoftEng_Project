# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginScreen.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

import sys
sys.path.append('../')
from BL.AccountR_W import VerifyCredentials
from LoginErr import LoginError
from DAL.Signup import User_signup
from DAL.MainDB import MainDatabase
from DAL.Check_Acc_from_DB import DB_access

class Ui_LoginScreen(object):
      

    def showMainDB(self):
        self.window = QtWidgets.QMainWindow()
        self.MainDB = MainDatabase()
        self.MainDB.MainUi(self.window)
        self.window.show()
        
    def signupcheck(self):
        print("register is pressed")
    
    def LoginError(self):
        self.window = QtWidgets.QDialog()
        self.err = LoginError()
        self.err.setupUi(self.window)
        self.window.show()


    def register(self):
        self.window = QtWidgets.QDialog()
        self.reg = User_signup()
        self.reg.setupUi(self.window)
        self.window.show()


    
    def setupUi(self, LoginScreen):
        LoginScreen.setObjectName("LoginScreen")
        LoginScreen.resize(793, 478)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Merk/Desktop/HokeysDotaIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoginScreen.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(LoginScreen)
        self.label.setGeometry(QtCore.QRect(220, 10, 381, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(LoginScreen)
        self.label_2.setGeometry(QtCore.QRect(290, 60, 231, 41))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(LoginScreen)
        self.pushButton.setGeometry(QtCore.QRect(340, 320, 93, 28))
        self.pushButton.setObjectName("pushButton")


        
        self.pushButton_2 = QtWidgets.QPushButton(LoginScreen)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 410, 171, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        
###### event to register user ########
        self.pushButton_2.clicked.connect(self.register)
        
        

########
        self.label_3 = QtWidgets.QLabel(LoginScreen)
        self.label_3.setGeometry(QtCore.QRect(330, 370, 141, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(LoginScreen)
        self.label_4.setGeometry(QtCore.QRect(180, 180, 81, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(LoginScreen)
        self.label_5.setGeometry(QtCore.QRect(180, 240, 81, 41))
        self.label_5.setObjectName("label_5")   
        self.lineEdit = QtWidgets.QLineEdit(LoginScreen)
        self.lineEdit.setGeometry(QtCore.QRect(280, 180, 231, 31))
        self.lineEdit.setObjectName("lineEdit")
        Username = self.lineEdit.text()
       

        self.lineEdit_2 = QtWidgets.QLineEdit(LoginScreen)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 250, 231, 31))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setMaxLength(32767)
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        Password = self.lineEdit_2.text()
        self.retranslateUi(LoginScreen)
        QtCore.QMetaObject.connectSlotsByName(LoginScreen)



        #########    Login Event Initiates   ##############
        self.pushButton.clicked.connect(self.getCredentials)
        
        ###################################################
                                        
        
        
        
        
        

    def retranslateUi(self, LoginScreen):
        _translate = QtCore.QCoreApplication.translate
        LoginScreen.setWindowTitle(_translate("LoginScreen", "User Login"))
        self.label.setText(_translate("LoginScreen", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">INVENTORY A+</span></p></body></html>"))
        self.label_2.setText(_translate("LoginScreen", "<html><head/><body><p><span style=\" font-size:11pt;\">A Simple Inventory Manager</span></p></body></html>"))
        self.pushButton.setText(_translate("LoginScreen", "Login"))
        self.pushButton_2.setText(_translate("LoginScreen", "Sign up "))
        self.label_3.setText(_translate("LoginScreen", "Not yet a member?"))
        self.label_4.setText(_translate("LoginScreen", "<html><head/><body><p><span style=\" font-size:10pt;\">Username:</span></p></body></html>"))
        self.label_5.setText(_translate("LoginScreen", "<html><head/><body><p><span style=\" font-size:10pt;\">Password:</span></p></body></html>"))
        
    def getCredentials(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        VerifyCredentials.AskDatabase(username,password)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginScreen = QtWidgets.QDialog()
    ui = Ui_LoginScreen()
    ui.setupUi(LoginScreen)
    LoginScreen.show()
    sys.exit(app.exec_())



