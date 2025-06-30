# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import QTimer, Signal
from user_manager import UserManager
from ui_login import Ui_LoginWindow

#add
from mainwindow import MainWindow
class loginWindow(QWidget):
    login_success = Signal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.ui.login.clicked.connect(self.login)
        self.ui.register_2.clicked.connect(self.register)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.usermanager = UserManager()
        self.setStyleSheet("""
                QWidget {
                    background-color: #fffdf8; /* 整体背景（浅奶油色） */
                    font-family: 'Arial';
                    font-size: 16px;
                    font-weight: bold;
                }

                QLineEdit {
                    background-color: #fefefe; /* 输入框背景 */
                    border: 1px solid #ccc;
                    border-radius: 8px;
                    padding: 4px;
                }

                QLabel {
                    color: #333333;
                }
                """)

    def login(self):
        self.usrname = self.ui.username.text()
        pwd = self.ui.password.text()
        status, msg = self.usermanager.try_login(self.usrname,pwd)
        if status == False:
            QMessageBox.warning(self, "警告", msg)
        if status == True:
            welcomeText = f"欢迎{self.usrname}!"
            self.ui.welcome.setText(welcomeText)
            self.ui.stackedWidget.setCurrentIndex(1)
            QTimer.singleShot(1000,lambda: self.login_signal())

    def login_signal(self):
        self.login_success.emit(self.usrname)
        self.close()

    def register(self):
        usrname = self.ui.username.text()
        pwd = self.ui.password.text()
        status, msg = self.usermanager.try_register(usrname,pwd)
