# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'selectAvatar.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QGridLayout, QHBoxLayout, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Avatar(object):
    def setupUi(self, Avatar):
        if not Avatar.objectName():
            Avatar.setObjectName(u"Avatar")
        Avatar.resize(400, 300)
        Avatar.setAutoFillBackground(False)
        self.buttonBox = QDialogButtonBox(Avatar)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 250, 341, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.frame = QFrame(Avatar)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 10, 350, 238))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(350, 200))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(0, 150))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
#ifndef Q_OS_MAC
        self.gridLayout.setSpacing(-1)
#endif
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.av5 = QPushButton(self.frame_2)
        self.av5.setObjectName(u"av5")
        sizePolicy.setHeightForWidth(self.av5.sizePolicy().hasHeightForWidth())
        self.av5.setSizePolicy(sizePolicy)
        self.av5.setMinimumSize(QSize(70, 70))
        self.av5.setMaximumSize(QSize(70, 70))

        self.gridLayout.addWidget(self.av5, 1, 1, 1, 1)

        self.av2 = QPushButton(self.frame_2)
        self.av2.setObjectName(u"av2")
        sizePolicy.setHeightForWidth(self.av2.sizePolicy().hasHeightForWidth())
        self.av2.setSizePolicy(sizePolicy)
        self.av2.setMinimumSize(QSize(70, 70))
        self.av2.setMaximumSize(QSize(70, 70))

        self.gridLayout.addWidget(self.av2, 0, 1, 1, 1)

        self.av4 = QPushButton(self.frame_2)
        self.av4.setObjectName(u"av4")
        sizePolicy.setHeightForWidth(self.av4.sizePolicy().hasHeightForWidth())
        self.av4.setSizePolicy(sizePolicy)
        self.av4.setMinimumSize(QSize(70, 70))
        self.av4.setMaximumSize(QSize(70, 70))

        self.gridLayout.addWidget(self.av4, 1, 0, 1, 1)

        self.av1 = QPushButton(self.frame_2)
        self.av1.setObjectName(u"av1")
        sizePolicy.setHeightForWidth(self.av1.sizePolicy().hasHeightForWidth())
        self.av1.setSizePolicy(sizePolicy)
        self.av1.setMinimumSize(QSize(70, 70))
        self.av1.setMaximumSize(QSize(70, 70))

        self.gridLayout.addWidget(self.av1, 0, 0, 1, 1)

        self.av6 = QPushButton(self.frame_2)
        self.av6.setObjectName(u"av6")
        sizePolicy.setHeightForWidth(self.av6.sizePolicy().hasHeightForWidth())
        self.av6.setSizePolicy(sizePolicy)
        self.av6.setMinimumSize(QSize(70, 70))
        self.av6.setMaximumSize(QSize(70, 70))

        self.gridLayout.addWidget(self.av6, 1, 2, 1, 1)

        self.av3 = QPushButton(self.frame_2)
        self.av3.setObjectName(u"av3")
        sizePolicy.setHeightForWidth(self.av3.sizePolicy().hasHeightForWidth())
        self.av3.setSizePolicy(sizePolicy)
        self.av3.setMinimumSize(QSize(70, 70))
        self.av3.setMaximumSize(QSize(70, 70))

        self.gridLayout.addWidget(self.av3, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.upload = QPushButton(self.frame_3)
        self.upload.setObjectName(u"upload")
        self.upload.setMinimumSize(QSize(0, 60))

        self.horizontalLayout.addWidget(self.upload)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(Avatar)
        self.buttonBox.accepted.connect(Avatar.accept)
        self.buttonBox.rejected.connect(Avatar.reject)

        QMetaObject.connectSlotsByName(Avatar)
    # setupUi

    def retranslateUi(self, Avatar):
        Avatar.setWindowTitle(QCoreApplication.translate("Avatar", u"Dialog", None))
        self.av5.setText("")
        self.av2.setText("")
        self.av4.setText("")
        self.av1.setText("")
        self.av6.setText("")
        self.av3.setText("")
        self.upload.setText(QCoreApplication.translate("Avatar", u"\u4e0a\u4f20\u6587\u4ef6\uff1a\u4e3a\u4e86\u5c3d\u53ef\u80fd\u597d\u7684\u663e\u793a\u6548\u679c\n"
"\u8bf7\u9009\u62e9\u6b63\u65b9\u5f62\u56fe\u7247", None))
    # retranslateUi

