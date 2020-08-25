from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(700, 500))
        MainWindow.setMaximumSize(QtCore.QSize(700, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
" \n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: rgba(128,128,128,0.5);\n"
"    border-radius: 10px;\n"
"    /*height: 15px;*/\n"
"    /*margin: 0px 20px 0 20px;*/\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    border-radius: 6px;\n"
"    background-color: #aaaaaa;\n"
"    min-width: 1px;\n"
"    min-height: 100px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: transparent;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"\n"
"QSlider::groove:vertical {\n"
"\n"
"\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 701, 511))
        self.label_3.setText("")
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setPixmap(QtGui.QPixmap("res/earth_b.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.label_passwordarchive = QtWidgets.QLabel(self.centralwidget)
        self.label_passwordarchive.setGeometry(QtCore.QRect(520, 20, 221, 81))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        self.label_passwordarchive.setFont(font)
        self.label_passwordarchive.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_passwordarchive.setStyleSheet("")
        self.label_passwordarchive.setAlignment(QtCore.Qt.AlignCenter)
        self.label_passwordarchive.setObjectName("label_passwordarchive")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(530, 10, 141, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #ffffff;")
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 70, 671, 20))
        self.line.setStyleSheet("color:white;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 20, 251, 41))
        self.label_4.setObjectName("label_4")
        self.pushButton_logout = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_logout.setGeometry(QtCore.QRect(250, 440, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_logout.setFont(font)
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(300, 100, 80, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setStyleSheet("border-radius:15px;\n"
"")
        self.pushButton_add.setObjectName("pushButton_add")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 171, 631, 261))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("border-radius: 10px;\n"
"background-color:rgba(200,200,200,0.3);\n"
"color: white;")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableWidget.setLineWidth(4)
        self.tableWidget.setMidLineWidth(5)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setWhatsThis(_translate("MainWindow", "Password must contain atleast 8 characters"))
        self.label_passwordarchive.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Berlin Sans FB\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:18pt; color:#33df33;\"> </span><span style=\" font-size:18pt; color:#ffffff;\">Λ</span><span style=\" font-family:\'Calibri (body)\'; font-size:18pt; color:#ffffff;\"> R </span><span style=\" font-family:\'Calibri (Body)\'; font-size:18pt; color:#ffffff;\">C H I V Ξ </span><span style=\" font-family:\'Calibri\'; font-size:18pt; color:#ffffff; vertical-align:super;\">™</span><span style=\" font-family:\'Calibri\'; font-size:18pt;\">             </span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Calibri\'; font-size:20pt; font-weight:600; color:#24f100;\">Password</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "U S E R :"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_logout.setText(_translate("MainWindow", "L O G O U T"))
        self.pushButton_add.setText(_translate("MainWindow", "+"))
