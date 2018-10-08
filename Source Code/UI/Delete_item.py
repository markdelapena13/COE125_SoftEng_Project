# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Delete_item.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append("../")
from BL.RemoveFromMainDB import MainDBDelete
class Deleteitem(object):
    def NewItemWindow(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 200)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 140, 461, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 40, 121, 41))
        self.label.setObjectName("label")

        self.item_name = QtWidgets.QLineEdit(Dialog)
        self.item_name.setGeometry(QtCore.QRect(160, 50, 231, 31))
        self.item_name.setObjectName("item_name")

        self.retranslateUi(Dialog)
        ## event that deletes item from database ##
        self.buttonBox.accepted.connect(self.getItemDetails)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Delete Item"))
        self.label.setText(_translate("Dialog", "Item Name:"))

    def getItemDetails(self):
        thingName = self.item_name.text()
        MainDBDelete.Delete_Items(thingName)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Deleteitem()
    ui.NewItemWindow(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

