from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(700, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(700, 500))
        MainWindow.setMaximumSize(QtCore.QSize(700, 500))
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet(" background-color: rgba(0,0,0,0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.489, y1:1, x2:0.483, y2:0, stop:0.0454545 rgba(0, 0, 0, 0), stop:0.704545 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 55));\n"
"}\n"
"\n"
"QPushButton{\n"
"    color: #ffffff;\n"
"    background-color: rgba(200,200,200, 0.3);\n"
"    border: 3px solid transparent;\n"
"    border-left: 5px transparent;\n"
"    border-right: 5px transparent;\n"
"    border-radius: 14px;\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"     border: 5px solid #0022ff;\n"
"    border-left: 5px transparent;\n"
"    border-right: 5px transparent;\n"
"    color: rgba(100,100,100,1);\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 3px solid #00ff22;\n"
"    border-left: 3px transparent;\n"
"    border-right: 3px transparent;\n"
"}\n"
"\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"\n"
"QMainWindow{\n"
"    background-color: qlineargradient(spread:pad, x1:0.489, y1:1, x2:0.483, y2:0, stop:0.0454545 rgba(0, 0, 0, 0), stop:0.704545 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 55));\n"
"}\n"
" \n"
"\n"
" ")
        self.centralwidget.setObjectName("centralwidget")
        self.label_passwordarchive = QtWidgets.QLabel(self.centralwidget)
        self.label_passwordarchive.setGeometry(QtCore.QRect(30, 0, 641, 131))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        self.label_passwordarchive.setFont(font)
        self.label_passwordarchive.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_passwordarchive.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.489, y1:1, x2:0.483, y2:0, stop:0.0454545 rgba(0, 0, 0, 0), stop:0.494318 rgba(0, 0, 0, 109), stop:0.892045 rgba(0, 0, 0, 255));")
        self.label_passwordarchive.setAlignment(QtCore.Qt.AlignCenter)
        self.label_passwordarchive.setObjectName("label_passwordarchive")
        self.pushButton_signin = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_signin.setGeometry(QtCore.QRect(170, 270, 350, 50))
        self.pushButton_signin.setMinimumSize(QtCore.QSize(80, 50))
        self.pushButton_signin.setMaximumSize(QtCore.QSize(350, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_signin.setFont(font)
        self.pushButton_signin.setStyleSheet("")
        self.pushButton_signin.setObjectName("pushButton_signin")
        self.pushButton_signup = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_signup.setGeometry(QtCore.QRect(170, 170, 350, 50))
        self.pushButton_signup.setMinimumSize(QtCore.QSize(80, 50))
        self.pushButton_signup.setMaximumSize(QtCore.QSize(350, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_signup.setFont(font)
        self.pushButton_signup.setStyleSheet("")
        self.pushButton_signup.setObjectName("pushButton_signup")
        self.label_bgimg = QtWidgets.QLabel(self.centralwidget)
        self.label_bgimg.setGeometry(QtCore.QRect(0, 0, 701, 501))
        self.label_bgimg.setStyleSheet("")
        self.label_bgimg.setText("")
        self.label_bgimg.setPixmap(QtGui.QPixmap("res/earth.jpg"))
        self.label_bgimg.setObjectName("label_bgimg")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 10, 141, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_bgimg.raise_()
        self.label_passwordarchive.raise_()
        self.pushButton_signin.raise_()
        self.pushButton_signup.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password ARCHIVE"))
        self.label_passwordarchive.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Berlin Sans FB\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; color:#ffffff;\">Λ</span><span style=\" font-family:\'Calibri (body)\'; font-size:22pt; color:#ffffff;\"> R </span><span style=\" font-family:\'Calibri (Body)\'; font-size:22pt; color:#ffffff;\">C H I V Ξ </span><span style=\" font-family:\'Calibri\'; font-size:22pt; color:#ffffff; vertical-align:super;\">™</span><span style=\" font-family:\'Calibri\'; font-size:12pt;\"> </span></p></body></html>"))
        self.pushButton_signin.setText(_translate("MainWindow", "S I G Π  I Π"))
        self.pushButton_signup.setText(_translate("MainWindow", "S I G Π  U P"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Calibri\'; font-size:20pt; font-weight:600; color:#24f100;\">Password</span></p></body></html>"))
