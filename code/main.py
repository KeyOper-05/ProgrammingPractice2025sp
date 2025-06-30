# This Python file uses the following encoding: utf-8
import sys
import os

# 设置 Qt 插件路径
from PySide6.QtWidgets import QApplication
from loginWindow import loginWindow

from mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication([])

    login = loginWindow()
    main=MainWindow()

    login.login_success.connect(lambda name:(
        main.setuser(name),
        main.show())
    )
    login.show()

    app.exec()
