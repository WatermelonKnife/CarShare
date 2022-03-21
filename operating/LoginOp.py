import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

from operating.dbop import DB
from operating.index import MainApp

import hashlib

login, _ = loadUiType('../staticUI/Login.ui')
enroll, _ = loadUiType('../staticUI/enroll.ui')


class LoginAPP(QMainWindow, login):
    usertype = ""

    def __init__(self):
        QMainWindow.__init__(self)

        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.handle_login)
        self.pushButton.clicked.connect(self.handle_enroll)

        self.register_app = EnrollApp()

    def handle_login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        password = hashlib.md5(bytes(password, encoding="utf-8"))
        password = password.hexdigest()
        d = DB()
        sql = "select * from user where name = %s and password = %s"
        result = d.search_db(sql, (username, password))
        print(result)

        if result:
            self.close()
            self.main_app = MainApp(username, result[0][4], self.changetype(result[0][3])
                                    )

            self.main_app.show()
        else:
            warning = QMessageBox.warning(self, "登录", "用户名或密码不正确!",
                                          QMessageBox.Yes)

    def handle_enroll(self):
        self.register_app.show()

    def changetype(self, s):
        if s == "user":
            return "乘客"
        else:
            if s == "driver":
                return "司机"
            else:
                if s == "manager":
                    return "管理员"


class EnrollApp(QMainWindow, enroll):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.routebutton.clicked.connect(self.handle_register)
        self.routebutton_2.clicked.connect(self.handle_quit)

    def handle_register(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        password = hashlib.md5(bytes(password, encoding="utf-8"))
        password = password.hexdigest()
        tel = self.lineEdit_3.text()
        usertype = self.comboBox.currentText()
        d = DB()
        usertype = self.changeType(usertype)
        if username and password and tel:
            sql = "insert into user(name,password,type,tel) values (%s,%s,%s,%s)"
            d.fix_db(sql, (username, password, usertype, tel))
            warning = QMessageBox.warning(self, "注册", "注册成功",
                                          QMessageBox.Yes)
            if warning == QMessageBox.Yes:
                self.close()
        else:
            warning = QMessageBox.warning(self, "注册", "请完善您的信息!",
                                          QMessageBox.Yes)

    def changeType(self, s):
        if s == "乘客":
            return "user"
        else:
            if s == "司机":
                return "driver"
            else:
                if s == "管理员":
                    return "manager"

    def handle_quit(self):
        self.close()


def main():
    app = QApplication([])
    window = LoginAPP()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
