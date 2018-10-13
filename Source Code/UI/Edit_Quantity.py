# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Edit_Quantity.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append("../")
from BL.EditQuantityFromMainDB import MainDBEdit
class Edititem(object):
    def EditUI(self, Dialog):
            Dialog.setObjectName("Dialog")
            Dialog.resize(480, 200)
            self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
            self.buttonBox.setGeometry(QtCore.QRect(10, 140, 461, 32))
            self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
            self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
            self.buttonBox.setCenterButtons(True)

            self.buttonBox.setObjectName("buttonBox")
            self.label = QtWidgets.QLabel(Dialog)
            self.label.setGeometry(QtCore.QRect(70, 40, 121, 41))
            self.label.setObjectName("label")
            self.label_2 = QtWidgets.QLabel(Dialog)
            self.label_2.setGeometry(QtCore.QRect(70, 80, 141, 41))
            self.label_2.setObjectName("label_2")

            self.item_name = QtWidgets.QLineEdit(Dialog)
            self.item_name.setGeometry(QtCore.QRect(160, 50, 231, 31))
            self.item_name.setObjectName("item_name")

            self.item_number = QtWidgets.QSpinBox(Dialog)
            self.item_number.setGeometry(QtCore.QRect(160, 90, 231, 31))
            self.item_number.setObjectName("item_number")

            self.retranslateUi(Dialog)
            ##get the name##
            self.buttonBox.accepted.connect(self.getItemDetails)

            
            self.buttonBox.accepted.connect(Dialog.accept)
            self.buttonBox.rejected.connect(Dialog.reject)
            QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
            _translate = QtCore.QCoreApplication.translate
            Dialog.setWindowTitle(_translate("Dialog", "Edit Quantity"))
            self.label.setText(_translate("Dialog", "Item to edit:"))
            self.label_2.setText(_translate("Dialog", "Item Quantity:"))

            
    def getItemDetails(self):
            thingName = self.item_name.text()
            thingNumber = self.item_number.text()
            MainDBEdit.Edit_Quantity(thingName,thingNumber)
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Edititem()
    ui.EditUI(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

