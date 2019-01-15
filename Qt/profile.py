# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profile.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_profile(object):
    def setupUi(self, profile):
        profile.setObjectName("profile")
        profile.setFixedSize(734, 486)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        profile.setWindowIcon(icon)
        profile.setStyleSheet("QLabel#room,#xlsx{\n"
"font-family:\"Comic Sans MS\",cursive,sans-serif;\n"
"border:solid;\n"
"border-width:1px;\n"
"border-color:black;\n"
"}\n"
"QLabel#xlsx:hover, #room:hover{\n"
"background-color:grey;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(profile)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 380, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.imgRoom = QtWidgets.QLabel(self.centralwidget)
        self.imgRoom.setGeometry(QtCore.QRect(230, 150, 91, 81))
        self.imgRoom.setToolTip("")
        self.imgRoom.setToolTipDuration(5)
        self.imgRoom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.imgRoom.setText("")
        self.imgRoom.setPixmap(QtGui.QPixmap(":/edit.png"))
        self.imgRoom.setScaledContents(True)
        self.imgRoom.setObjectName("imgRoom")
        self.imgUpload = QtWidgets.QLabel(self.centralwidget)
        self.imgUpload.setGeometry(QtCore.QRect(400, 150, 101, 81))
        self.imgUpload.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.imgUpload.setText("")
        self.imgUpload.setPixmap(QtGui.QPixmap(":/upload.png"))
        self.imgUpload.setScaledContents(True)
        self.imgUpload.setObjectName("imgUpload")
        self.room = QtWidgets.QLabel(self.centralwidget)
        self.room.setGeometry(QtCore.QRect(200, 250, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS,cursive,sans-serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.room.setFont(font)
        self.room.setAlignment(QtCore.Qt.AlignCenter)
        self.room.setObjectName("room")
        self.xlsx = QtWidgets.QLabel(self.centralwidget)
        self.xlsx.setGeometry(QtCore.QRect(390, 250, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS,cursive,sans-serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.xlsx.setFont(font)
        self.xlsx.setAlignment(QtCore.Qt.AlignCenter)
        self.xlsx.setObjectName("xlsx")
        self.profileSeat = QtWidgets.QLabel(self.centralwidget)
        self.profileSeat.setGeometry(QtCore.QRect(260, 30, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.profileSeat.setFont(font)
        self.profileSeat.setAlignment(QtCore.Qt.AlignCenter)
        self.profileSeat.setObjectName("profileSeat")
        profile.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(profile)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 734, 21))
        self.menubar.setObjectName("menubar")
        profile.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(profile)
        self.statusbar.setObjectName("statusbar")
        profile.setStatusBar(self.statusbar)
        self.room.setBuddy(self.imgRoom)
        self.xlsx.setBuddy(self.imgUpload)

        self.retranslateUi(profile)
        QtCore.QMetaObject.connectSlotsByName(profile)

    def retranslateUi(self, profile):
        _translate = QtCore.QCoreApplication.translate
        profile.setWindowTitle(_translate("profile", "Exam Seat Planner"))
        self.pushButton.setText(_translate("profile", "Past seat plans"))
        self.room.setText(_translate("profile", "<html><head/><body><p>Edit Room Profile</p></body></html>"))
        self.xlsx.setText(_translate("profile", "<html><head/><body><p><span style=\" font-size:12pt;\">Upload XLSX </span></p></body></html>"))
        self.profileSeat.setText(_translate("profile", "Exam Seat Planner"))

import images.resources

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    profile = QtWidgets.QMainWindow()
    ui = Ui_profile()
    ui.setupUi(profile)
    profile.show()
    sys.exit(app.exec_())

