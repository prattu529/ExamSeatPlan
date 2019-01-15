# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditRoomProfile.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_editProfile(object):
    def setupUi(self, editProfile):
        editProfile.setObjectName("editProfile")
        editProfile.resize(561, 410)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        editProfile.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(editProfile)
        self.buttonBox.setGeometry(QtCore.QRect(140, 320, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.table = QtWidgets.QLabel(editProfile)
        self.table.setGeometry(QtCore.QRect(90, 40, 301, 261))
        self.table.setStyleSheet("\n"
"")
        self.table.setAlignment(QtCore.Qt.AlignCenter)
        self.table.setObjectName("table")

        self.retranslateUi(editProfile)
        self.buttonBox.accepted.connect(editProfile.accept)
        self.buttonBox.clicked['QAbstractButton*'].connect(editProfile.close)
        QtCore.QMetaObject.connectSlotsByName(editProfile)

    def retranslateUi(self, editProfile):
        _translate = QtCore.QCoreApplication.translate
        editProfile.setWindowTitle(_translate("editProfile", "Edit Room Profile"))
        self.table.setText(_translate("editProfile", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:16px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:500; margin-bottom:50px;\">Edit Room Profile</span> </p>\n"
"<table border=\"1\" style=\" border-color:black; margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" align=\"center\" cellspacing=\"0\" cellpadding=\"10\">\n"
"<tr>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Room</span></p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">No. of seats</span></p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">No. of students</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Lab1</p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25</p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20</p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Lab2</p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">30</p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">28</p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Lab3</p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">40</p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">40</p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Lab4</p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">30</p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25</p></td></tr></table></body></html>"))

import images.resources

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    editProfile = QtWidgets.QDialog()
    ui = Ui_editProfile()
    ui.setupUi(editProfile)
    editProfile.show()
    sys.exit(app.exec_())

