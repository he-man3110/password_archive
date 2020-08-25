from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

class Ui_addcred(QDialog):
    def __init__(self):
        super().__init__()
        self.setObjectName("Add credentials")
        self.resize(480, 338)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(480, 338))
        self.setMaximumSize(QtCore.QSize(483, 338))
        self.setStyleSheet("QDialog {\n"
"background-color: black;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"background-color: white;\n"
"border-radius:24px;\n"
"color: black;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border: 3px solid black;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: white;\n"
"    border: 2px solid black;\n"
"    border-radius: 20px;\n"
"    background-color: #24f100;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border: 5px solid #24f100;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"border:5px solid black;\n"
"color: black;\n"
"}")
        self.lineEdit_appname = QtWidgets.QLineEdit(self)
        self.lineEdit_appname.setGeometry(QtCore.QRect(120, 50, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_appname.setFont(font)
        self.lineEdit_appname.setStyleSheet("")
        self.lineEdit_appname.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_appname.setObjectName("lineEdit_appname")
        self.lineEdit_password = QtWidgets.QLineEdit(self)
        self.lineEdit_password.setGeometry(QtCore.QRect(80, 140, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet("")
        self.lineEdit_password.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.pushButton_save = QtWidgets.QPushButton(self)
        self.pushButton_save.setGeometry(QtCore.QRect(150, 250, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setObjectName("pushButton_save")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 200, 481, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color:red;")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        QtCore.QMetaObject.connectSlotsByName(self)
        self.retranslateUi(self)
        self.pushButton_save.clicked.connect(self.grab_details)
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit_appname.setPlaceholderText(_translate("Dialog", "App Name"))
        self.lineEdit_password.setPlaceholderText(_translate("Dialog", "Password"))
        self.pushButton_save.setText(_translate("Dialog", "save"))

    def grab_details(self):
        appname = self.lineEdit_appname.text()
        password = self.lineEdit_password.text()
        #verify if password is valid i.e not empty
        if appname == "":
            self.label.setText("Provide an App Name!")
        elif len(password) < 8:
            self.label.setText("Invalid Password! (Minimum 8 characters)")
        else:
            self.accept()



        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_addcred()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
