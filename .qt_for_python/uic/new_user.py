# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Dell\Downloads\register-system-main\register-system-main\new_user.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_New_User(object):
    def setupUi(self, New_User):
        New_User.setObjectName("New_User")
        New_User.resize(657, 943)
        New_User.setStyleSheet("color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(New_User)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.background = QtWidgets.QFrame(self.centralwidget)
        self.background.setStyleSheet("background-color: rgb(34, 40, 49);")
        self.background.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background.setObjectName("background")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.background)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.login_area = QtWidgets.QFrame(self.background)
        self.login_area.setEnabled(True)
        self.login_area.setMaximumSize(QtCore.QSize(450, 600))
        self.login_area.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(57, 62, 70);")
        self.login_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_area.setObjectName("login_area")
        self.lineEdit = QtWidgets.QLineEdit(self.login_area)
        self.lineEdit.setGeometry(QtCore.QRect(100, 200, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Swis721 Cn BT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(221, 221, 221);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 40, 49);\n"
"    color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(0, 173, 181);\n"
"    \n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 173, 181);    \n"
"    color: rgb(0, 173, 181);\n"
"}")
        self.lineEdit.setMaxLength(32)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.login_area)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 320, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Swis721 Cn BT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(221, 221, 221);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 40, 49);\n"
"    color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(0, 173, 181);\n"
"    \n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 173, 181);    \n"
"    color: rgb(0, 173, 181);\n"
"}")
        self.lineEdit_3.setMaxLength(15)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.login_area)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 480, 250, 51))
        font = QtGui.QFont()
        font.setFamily("Swis721 Cn BT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background-color: rgb(34, 40, 49);\n"
"    border: 2px solid rgb(57, 62, 70);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 173, 181);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(30, 200, 190);\n"
"    border-radius: 5px;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.login_area)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 260, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Swis721 Cn BT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(221, 221, 221);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 40, 49);\n"
"    color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(0, 173, 181);\n"
"    \n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 173, 181);    \n"
"    color: rgb(0, 173, 181);\n"
"}")
        self.lineEdit_2.setMaxLength(32)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.login_area)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 380, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Swis721 Cn BT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(221, 221, 221);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 40, 49);\n"
"    color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(0, 173, 181);\n"
"    \n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 173, 181);    \n"
"    color: rgb(0, 173, 181);\n"
"}")
        self.lineEdit_4.setMaxLength(15)
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.checkBox = QtWidgets.QCheckBox(self.login_area)
        self.checkBox.setGeometry(QtCore.QRect(100, 440, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Swis721 Cn BT")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("QCheckBox::indicator{\n"
"    border: 3px solid rgb(0, 173, 181);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(30, 40, 49);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"    border: 3px solid rgb(0, 173, 181);\n"
"    border-radius: 10px;\n"
"    background-color: rgb(25, 193, 200);\n"
"}\n"
"\n"
"\n"
"")
        self.checkBox.setObjectName("checkBox")
        self.label_2 = QtWidgets.QLabel(self.login_area)
        self.label_2.setGeometry(QtCore.QRect(80, 540, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Swis721 Cn BT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(166, 0, 0);")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.login_area)
        self.label_3.setGeometry(QtCore.QRect(150, 30, 161, 141))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("c:\\Users\\Dell\\Downloads\\register-system-main\\register-system-main\\logo.png"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.login_area)
        self.verticalLayout.addWidget(self.background)
        New_User.setCentralWidget(self.centralwidget)

        self.retranslateUi(New_User)
        QtCore.QMetaObject.connectSlotsByName(New_User)

    def retranslateUi(self, New_User):
        _translate = QtCore.QCoreApplication.translate
        New_User.setWindowTitle(_translate("New_User", "Register"))
        self.lineEdit.setPlaceholderText(_translate("New_User", "NAME"))
        self.lineEdit_3.setPlaceholderText(_translate("New_User", "PASSWORD"))
        self.pushButton_2.setText(_translate("New_User", "REGISTER"))
        self.lineEdit_2.setPlaceholderText(_translate("New_User", "USER"))
        self.lineEdit_4.setPlaceholderText(_translate("New_User", "CONFIRM PASSWORD"))
        self.checkBox.setText(_translate("New_User", "I AGREE WITH THE TERMS AND CONDITIONS."))
import logo_rc
