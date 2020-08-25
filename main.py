from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget
from PyQt5 import QtCore, QtWidgets
from PyQt5.Qt import QTableWidgetItem
import sys
import startingpage
import signuppage
import signinpage
import siusage
import add_cred
import encryption_engine

class PasswordArchive(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_main = startingpage.Ui_MainWindow()
        self.ui_su = signuppage.Ui_SignUpPage()
        self.ui_si = signinpage.Ui_SignInPage()
        self.ui_siu = siusage.Ui_MainWindow() 

        self.new_window = None
        self.current_user = None
        self.info = None
        self.view_main()

    def view_main(self):
        self.ui_main.setupUi(self)
        self.ui_main.pushButton_signup.clicked.connect(self.view_signuppage)
        self.ui_main.pushButton_signin.clicked.connect(self.view_signinpage)
        self.show()

    def view_signuppage(self):
        self.ui_su = signuppage.Ui_SignUpPage()
        self.ui_su.setupUi(self)
        self.ui_su.pushButton_back.clicked.connect(self.view_main)
        self.ui_su.pushButton_create.clicked.connect(self.create_profile)
        self.show()
        
    def view_signinpage(self):
        #self.current_user = None 
        self.ui_si.setupUi(self)
        self.ui_si.pushButton_back.clicked.connect(self.view_main)
        self.ui_si.pushButton_login.clicked.connect(self.on_login)
        self.show()

    def view_usagepage(self):
        self.ui_siu.setupUi(self)
        self.ui_siu.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.ui_siu.tableWidget.setColumnCount(2)
        self.ui_siu.tableWidget.setColumnWidth(0,183)
        self.ui_siu.tableWidget.setColumnWidth(1,461)
        self.ui_siu.pushButton_logout.clicked.connect(self.view_signinpage)
        self.ui_siu.pushButton_add.clicked.connect(self.add_data)
        self.credentials_update()
        self.show()
    
    def add_data(self, checked):
        dlg_ui = add_cred.Ui_addcred()
        dlg_ui.setWindowModality(QtCore.Qt.ApplicationModal)
        if dlg_ui.exec_() == QtWidgets.QDialog.Accepted:
            p,a = dlg_ui.lineEdit_password.text(), dlg_ui.lineEdit_appname.text()
        encryption_engine.add_to_vault(self.current_user,a,p)
        self.view_usagepage()

    def create_profile(self):
        name = self.ui_su.lineEdit_name.text()
        email = self.ui_su.lineEdit_email.text()
        p = self.ui_su.lineEdit_password.text()
        phone = self.ui_su.lineEdit_phone.text()
        if name == "" or email == "" or p == "":
            self.disp_error_su("Please Enter all the fields.")
            return
        if p == self.ui_su.lineEdit_confpassword.text():
            ermsg = encryption_engine.recognize(name, email, phone, p)
            if ermsg != "Account Created!":
                self.disp_error_su(ermsg)
                return
            self.disp_error_su(ermsg)
        else:
            self.disp_error_su("Passwords do not match!")
            return
    
    def on_login(self):
        email = self.ui_si.lineEdit_email.text()
        password = self.ui_si.lineEdit_password.text()
        if encryption_engine.validate(email, password):
            self.current_user = email 
            self.view_usagepage()
        else:
            self.disp_error_si("Invalid Email or password!")
    
    def credentials_update(self):
        try:
            vault = open(encryption_engine.who_is(self.current_user), "r")
        except :
            vault = open(encryption_engine.who_is(self.current_user), "w")
        self.info = encryption_engine.get_user_cred(self.current_user)
        self.row_len = len(self.info)
        self.ui_siu.tableWidget.setRowCount(self.row_len)
        for i in range(self.row_len):
            for j in range(2):
                item  = QTableWidgetItem("  " + self.info[i][j])
                self.ui_siu.tableWidget.setItem(i,j,item)
        vault.close()

    def disp_error_su(self, string):
        self.ui_su.lineEdit_errmsg.setStyleSheet("border-radius:20px;color:red;background-color:rgba(0,0,0,1);")
        self.ui_su.lineEdit_errmsg.setText(string)
    
    def disp_error_si(self, string):
        self.ui_si.lineEdit_errmsg.setStyleSheet("border-radius:20px;color:red;background-color:rgba(0,0,0,1);")
        self.ui_si.lineEdit_errmsg.setText(string)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    app = PasswordArchive()
    app.show()
    sys.exit(App.exec_())

