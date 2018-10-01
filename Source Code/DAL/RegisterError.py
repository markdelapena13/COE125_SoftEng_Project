# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegisterError.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ERROR(object):
    def setupUi(self, ERROR):
        ERROR.setObjectName("ERROR")
        ERROR.resize(400, 300)
        self.label = QtWidgets.QLabel(ERROR)
        self.label.setGeometry(QtCore.QRect(0, 50, 411, 181))
        self.label.setObjectName("label")

        self.retranslateUi(ERROR)
        QtCore.QMetaObject.connectSlotsByName(ERROR)

    def retranslateUi(self, ERROR):
        _translate = QtCore.QCoreApplication.translate
        ERROR.setWindowTitle(_translate("ERROR", "Register Error"))
        self.label.setText(_translate("ERROR", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Account with this username already exists</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ERROR = QtWidgets.QWidget()
    ui = Ui_ERROR()
    ui.setupUi(ERROR)
    ERROR.show()
    sys.exit(app.exec_())

