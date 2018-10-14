# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Signup.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!
import sqlite3
import os.path
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append('../')
from UI.registerSucc import Succ
from UI.RegisterError import Ui_ERROR
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = "../../Database/InventoryDatabase.db"
conn=sqlite3.connect(db_path)

class User_signup(object):

    def registerSucc(self):
        self.window=QtWidgets.QDialog()
        self.succ = Succ()
        self.succ.setupUi(self.window)
        self.window.show()

    def registerUser(self):
        Username=self.UserEnter.text()
        connection = sqlite3.connect("../../Database/InventoryDatabase.db")
        result = connection.execute("SELECT * FROM User WHERE username = ?",(Username, ))
        rows = result.fetchall()
        if( len(rows) > 0):
            subprocess.call(['python','../UI/RegisterError.py'])

            
        else:
            Username=self.UserEnter.text()
            Password=self.PassEnter.text()
            sql="INSERT INTO User(username,password) VALUES(?,?)"
            cur=conn.cursor()
            values=(Username,Password)
            cur.execute(sql, values)
            conn.commit()
            conn.close()
            subprocess.call(['python','../UI/registerSucc.py'])

    def displayError(self):
        self.window=QtWidgets.QDialog()
        self.regerr= Ui_ERROR()
        self.regerr.setupUi(self.window)
        self.window.show()



    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(614, 378)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(60, 280, 461, 121))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.UserLabel = QtWidgets.QLabel(Dialog)
        self.UserLabel.setGeometry(QtCore.QRect(150, 40, 161, 41))
        self.UserLabel.setObjectName("UserLabel")
        self.PassLabel = QtWidgets.QLabel(Dialog)
        self.PassLabel.setGeometry(QtCore.QRect(150, 140, 131, 41))
        self.PassLabel.setObjectName("PassLabel")



        ####### Field to Enter Username #########
        self.UserEnter = QtWidgets.QLineEdit(Dialog)
        self.UserEnter.setGeometry(QtCore.QRect(150, 80, 271, 31))
        self.UserEnter.setObjectName("UserEnter")

        ######## Field to Enter Password #######

        self.PassEnter = QtWidgets.QLineEdit(Dialog)
        self.PassEnter.setGeometry(QtCore.QRect(150, 190, 281, 31))
        self.PassEnter.setObjectName("PassEnter")



        ####### button to register #########
        self.pushReg = QtWidgets.QPushButton(Dialog)
        self.pushReg.setGeometry(QtCore.QRect(230, 280, 121, 41))
        self.pushReg.setObjectName("pushReg")
        self.pushReg.clicked.connect(self.registerUser)
       





        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "User Registration"))
        self.UserLabel.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Desired Username:</span></p></body></html>"))
        self.PassLabel.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Password:</span></p></body></html>"))
        self.pushReg.setText(_translate("Dialog", "Register"))






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = User_signup() #class name of called file
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

