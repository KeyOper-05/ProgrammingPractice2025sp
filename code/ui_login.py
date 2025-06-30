# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.setEnabled(True)
        LoginWindow.resize(300, 214)
        self.horizontalLayout = QHBoxLayout(LoginWindow)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(LoginWindow)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.loginNreg = QWidget()
        self.loginNreg.setObjectName(u"loginNreg")
        self.verticalLayout = QVBoxLayout(self.loginNreg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.loginNreg)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.frame_6 = QFrame(self.loginNreg)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QSize(0, 40))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMinimumSize(QSize(60, 0))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.username = QLineEdit(self.frame_6)
        self.username.setObjectName(u"username")
        self.username.setMinimumSize(QSize(160, 20))

        self.horizontalLayout_5.addWidget(self.username)


        self.verticalLayout.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.loginNreg)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMinimumSize(QSize(0, 40))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, 6, 6, 6)
        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setMinimumSize(QSize(60, 0))
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.password = QLineEdit(self.frame_7)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(160, 20))

        self.horizontalLayout_6.addWidget(self.password)


        self.verticalLayout.addWidget(self.frame_7)

        self.frame_5 = QFrame(self.loginNreg)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QSize(0, 40))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.login = QPushButton(self.frame_5)
        self.login.setObjectName(u"login")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.login.sizePolicy().hasHeightForWidth())
        self.login.setSizePolicy(sizePolicy2)
        self.login.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_4.addWidget(self.login)

        self.register_2 = QPushButton(self.frame_5)
        self.register_2.setObjectName(u"register_2")
        sizePolicy2.setHeightForWidth(self.register_2.sizePolicy().hasHeightForWidth())
        self.register_2.setSizePolicy(sizePolicy2)
        self.register_2.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_4.addWidget(self.register_2)


        self.verticalLayout.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.loginNreg)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.welcome = QLabel(self.page_2)
        self.welcome.setObjectName(u"welcome")
        self.welcome.setGeometry(QRect(40, 50, 171, 71))
        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(LoginWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("LoginWindow", u"PKU Calendar", None))
        self.label_5.setText(QCoreApplication.translate("LoginWindow", u"\u7528\u6237\u540d", None))
        self.label_6.setText(QCoreApplication.translate("LoginWindow", u"\u5bc6\u7801", None))
        self.login.setText(QCoreApplication.translate("LoginWindow", u"Login", None))
        self.register_2.setText(QCoreApplication.translate("LoginWindow", u"Register", None))
        self.welcome.setText(QCoreApplication.translate("LoginWindow", u"TextLabel", None))
    # retranslateUi

