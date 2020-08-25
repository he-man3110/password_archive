from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignInPage(object):
    def setupUi(self, SignInPage):
        SignInPage.setObjectName("SignInPage")
        SignInPage.resize(700, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SignInPage.sizePolicy().hasHeightForWidth())
        SignInPage.setSizePolicy(sizePolicy)
        SignInPage.setMaximumSize(QtCore.QSize(700, 500))
        SignInPage.setSizeIncrement(QtCore.QSize(700, 500))
        self.centralwidget = QtWidgets.QWidget(SignInPage)
        self.centralwidget.setStyleSheet("QLineEdit {\n"
"    color: white;\n"
"    border-radius: 12px;\n"
"    padding: 0 8px;\n"
"    background-color:rgba(128,128,128,0);\n"
"    selection-background-color: blue;\n"
"}\n"
"\n"
"QPushButton{\n"
"    color: #000000;\n"
"    background-color: rgba(200,255,200, 0.3);\n"
"    border: 3px solid transparent;\n"
"    border-left: 5px transparent;\n"
"    border-right: 5px transparent;\n"
"    border-radius: 14px;\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 5px solid #0022ff;\n"
"    border-left: 5px transparent;\n"
"    border-right: 5px transparent;\n"
"    color: rgba(100,100,100,1);\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 3px solid #00ff22;\n"
"    border-left:3px transparent;\n"
"    border-right:3px transparent;\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
" ")
        self.centralwidget.setObjectName("centralwidget")
        self.label_bgimg = QtWidgets.QLabel(self.centralwidget)
        self.label_bgimg.setGeometry(QtCore.QRect(0, 0, 701, 511))
        self.label_bgimg.setText("")
        self.label_bgimg.setTextFormat(QtCore.Qt.RichText)
        self.label_bgimg.setPixmap(QtGui.QPixmap("res/earth_b.jpg"))
        self.label_bgimg.setScaledContents(True)
        self.label_bgimg.setWordWrap(False)
        self.label_bgimg.setObjectName("label_bgimg")
        self.label_passwordarchive = QtWidgets.QLabel(self.centralwidget)
        self.label_passwordarchive.setGeometry(QtCore.QRect(520, 20, 221, 81))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        self.label_passwordarchive.setFont(font)
        self.label_passwordarchive.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_passwordarchive.setStyleSheet("")
        self.label_passwordarchive.setAlignment(QtCore.Qt.AlignCenter)
        self.label_passwordarchive.setObjectName("label_passwordarchive")
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(590, 460, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_login = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_login.setGeometry(QtCore.QRect(250, 400, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setObjectName("pushButton_login")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(180, 320, 321, 3))
        self.line_5.setLineWidth(1)
        self.line_5.setMidLineWidth(2)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_email = QtWidgets.QLabel(self.centralwidget)
        self.label_email.setGeometry(QtCore.QRect(180, 170, 321, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_email.sizePolicy().hasHeightForWidth())
        self.label_email.setSizePolicy(sizePolicy)
        self.label_email.setMinimumSize(QtCore.QSize(321, 51))
        self.label_email.setMaximumSize(QtCore.QSize(321, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_email.setFont(font)
        self.label_email.setObjectName("label_email")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(180, 240, 321, 3))
        self.line_2.setMidLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(180, 250, 321, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_password.sizePolicy().hasHeightForWidth())
        self.label_password.setSizePolicy(sizePolicy)
        self.label_password.setMinimumSize(QtCore.QSize(321, 51))
        self.label_password.setMaximumSize(QtCore.QSize(321, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.label_caa = QtWidgets.QLabel(self.centralwidget)
        self.label_caa.setEnabled(True)
        self.label_caa.setGeometry(QtCore.QRect(180, 80, 321, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_caa.sizePolicy().hasHeightForWidth())
        self.label_caa.setSizePolicy(sizePolicy)
        self.label_caa.setMinimumSize(QtCore.QSize(321, 51))
        self.label_caa.setMaximumSize(QtCore.QSize(321, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_caa.setFont(font)
        self.label_caa.setAlignment(QtCore.Qt.AlignCenter)
        self.label_caa.setObjectName("label_caa")
        self.lineEdit_email = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_email.setGeometry(QtCore.QRect(170, 200, 321, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_email.sizePolicy().hasHeightForWidth())
        self.lineEdit_email.setSizePolicy(sizePolicy)
        self.lineEdit_email.setMinimumSize(QtCore.QSize(321, 41))
        self.lineEdit_email.setMaximumSize(QtCore.QSize(321, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_email.setFont(font)
        self.lineEdit_email.setStyleSheet("")
        self.lineEdit_email.setPlaceholderText("")
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(170, 280, 321, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_password.sizePolicy().hasHeightForWidth())
        self.lineEdit_password.setSizePolicy(sizePolicy)
        self.lineEdit_password.setMinimumSize(QtCore.QSize(321, 41))
        self.lineEdit_password.setMaximumSize(QtCore.QSize(321, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStatusTip("")
        self.lineEdit_password.setWhatsThis("")
        self.lineEdit_password.setStyleSheet("")
        self.lineEdit_password.setInputMask("")
        self.lineEdit_password.setText("")
        self.lineEdit_password.setFrame(True)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.bg_mesh = QtWidgets.QLabel(self.centralwidget)
        self.bg_mesh.setGeometry(QtCore.QRect(170, 150, 351, 201))
        self.bg_mesh.setStyleSheet("border-radius: 16px;\n"
"background-color: rgba(100,100,100,0.3);")
        self.bg_mesh.setText("")
        self.bg_mesh.setObjectName("bg_mesh")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(530, 10, 141, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit_errmsg = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_errmsg.setGeometry(QtCore.QRect(120, 351, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_errmsg.setFont(font)
        self.lineEdit_errmsg.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_errmsg.setReadOnly(True)
        self.lineEdit_errmsg.setObjectName("lineEdit_errmsg")
        self.label_bgimg.raise_()
        self.label_passwordarchive.raise_()
        self.pushButton_back.raise_()
        self.pushButton_login.raise_()
        self.label_caa.raise_()
        self.bg_mesh.raise_()
        self.label_email.raise_()
        self.label_password.raise_()
        self.line_2.raise_()
        self.line_5.raise_()
        self.lineEdit_email.raise_()
        self.lineEdit_password.raise_()
        self.label.raise_()
        self.lineEdit_errmsg.raise_()
        SignInPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(SignInPage)
        QtCore.QMetaObject.connectSlotsByName(SignInPage)

    def retranslateUi(self, SignInPage):
        _translate = QtCore.QCoreApplication.translate
        SignInPage.setWindowTitle(_translate("SignInPage", "MainWindow"))
        self.label_bgimg.setWhatsThis(_translate("SignInPage", "Password must contain atleast 8 characters"))
        self.label_passwordarchive.setText(_translate("SignInPage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Berlin Sans FB\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:18pt; color:#33df33;\"> </span><span style=\" font-size:18pt; color:#ffffff;\">Λ</span><span style=\" font-family:\'Calibri (body)\'; font-size:18pt; color:#ffffff;\"> R </span><span style=\" font-family:\'Calibri (Body)\'; font-size:18pt; color:#ffffff;\">C H I V Ξ </span><span style=\" font-family:\'Calibri\'; font-size:18pt; color:#ffffff; vertical-align:super;\">™</span><span style=\" font-family:\'Calibri\'; font-size:18pt;\">             </span></p></body></html>"))
        self.pushButton_back.setText(_translate("SignInPage", "B A C K >"))
        self.pushButton_login.setText(_translate("SignInPage", "L O G I N"))
        self.label_email.setText(_translate("SignInPage", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Email ID</span></p></body></html>"))
        self.label_password.setText(_translate("SignInPage", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Password </span></p></body></html>"))
        self.label_caa.setText(_translate("SignInPage", "<html><head/><body><p><span style=\" font-size:20pt; color:#ffffff;\">Login</span></p></body></html>"))
        self.lineEdit_password.setToolTip(_translate("SignInPage", "Password must contain atleast 8 characters.Spaces not allowed."))
        self.label.setText(_translate("SignInPage", "<html><head/><body><p><span style=\" font-family:\'Calibri\'; font-size:20pt; font-weight:600; color:#24f100;\">Password</span></p></body></html>"))
