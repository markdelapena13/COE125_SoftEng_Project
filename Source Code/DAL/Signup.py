# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Signup.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
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
        self.UserEnter = QtWidgets.QLineEdit(Dialog)
        self.UserEnter.setGeometry(QtCore.QRect(150, 80, 271, 31))
        self.UserEnter.setObjectName("UserEnter")
        self.PassEnter = QtWidgets.QLineEdit(Dialog)
        self.PassEnter.setGeometry(QtCore.QRect(150, 190, 281, 31))
        self.PassEnter.setObjectName("PassEnter")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(230, 280, 121, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "User Registration"))
        self.UserLabel.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Desired Username:</span></p></body></html>"))
        self.PassLabel.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Password:</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

