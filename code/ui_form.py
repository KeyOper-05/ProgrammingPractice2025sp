# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDateTimeEdit,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPlainTextEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(809, 642)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.riji = QWidget()
        self.riji.setObjectName(u"riji")
        self.verticalLayout_4 = QHBoxLayout(self.riji)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_4 = QWidget(self.riji)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(20, 10, 651, 131))
        self.widget_5.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.mon = QPushButton(self.widget_5)
        self.mon.setObjectName(u"mon")
        self.mon.setGeometry(QRect(10, 60, 81, 61))
        self.wed = QPushButton(self.widget_5)
        self.wed.setObjectName(u"wed")
        self.wed.setGeometry(QRect(190, 60, 81, 61))
        self.wed.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.tue = QPushButton(self.widget_5)
        self.tue.setObjectName(u"tue")
        self.tue.setGeometry(QRect(100, 60, 81, 61))
        self.thu = QPushButton(self.widget_5)
        self.thu.setObjectName(u"thu")
        self.thu.setGeometry(QRect(280, 60, 81, 61))
        self.fri = QPushButton(self.widget_5)
        self.fri.setObjectName(u"fri")
        self.fri.setGeometry(QRect(370, 60, 81, 61))
        self.sat = QPushButton(self.widget_5)
        self.sat.setObjectName(u"sat")
        self.sat.setGeometry(QRect(460, 60, 81, 61))
        self.sun = QPushButton(self.widget_5)
        self.sun.setObjectName(u"sun")
        self.sun.setGeometry(QRect(550, 60, 81, 61))
        self.pushButton_3 = QPushButton(self.widget_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(430, 10, 201, 31))
        font = QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.label_6 = QLabel(self.widget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 10, 101, 31))
        font1 = QFont()
        font1.setFamilies([u"Microsoft Tai Le"])
        font1.setPointSize(13)
        font1.setBold(True)
        self.label_6.setFont(font1)
        self.selectDate = QDateEdit(self.widget_5)
        self.selectDate.setObjectName(u"selectDate")
        self.selectDate.setGeometry(QRect(120, 11, 111, 31))
        self.pushButton_2 = QPushButton(self.widget_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(240, 10, 181, 31))
        self.pushButton_2.setFont(font)
        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(10, 130, 671, 451))
        self.input_text = QTextEdit(self.widget_6)
        self.input_text.setObjectName(u"input_text")
        self.input_text.setGeometry(QRect(10, 60, 321, 331))
        self.input_text.setMaximumSize(QSize(16777215, 16777215))
        self.input_text.setFont(font)
        self.save_button = QPushButton(self.widget_6)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(350, 20, 141, 51))
        self.ai_analyse = QTextEdit(self.widget_6)
        self.ai_analyse.setObjectName(u"ai_analyse")
        self.ai_analyse.setGeometry(QRect(350, 80, 301, 311))
        self.produce_report = QPushButton(self.widget_6)
        self.produce_report.setObjectName(u"produce_report")
        self.produce_report.setGeometry(QRect(500, 20, 151, 51))
        self.inform_text = QLabel(self.widget_6)
        self.inform_text.setObjectName(u"inform_text")
        self.inform_text.setGeometry(QRect(10, 20, 331, 31))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.inform_text.setFont(font2)
        self.generate_graph_button = QPushButton(self.widget_6)
        self.generate_graph_button.setObjectName(u"generate_graph_button")
        self.generate_graph_button.setGeometry(QRect(350, 400, 301, 41))
        self.inform_text2 = QLabel(self.widget_6)
        self.inform_text2.setObjectName(u"inform_text2")
        self.inform_text2.setGeometry(QRect(10, 400, 331, 31))
        font3 = QFont()
        font3.setFamilies([u"Gill Sans MT"])
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(False)
        self.inform_text2.setFont(font3)

        self.verticalLayout_4.addWidget(self.widget_4)

        self.stackedWidget.addWidget(self.riji)
        self.daiban = QWidget()
        self.daiban.setObjectName(u"daiban")
        self.horizontalLayout = QHBoxLayout(self.daiban)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.daiban)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_2)

        self.today = QDateEdit(self.frame)
        self.today.setObjectName(u"today")

        self.verticalLayout_5.addWidget(self.today)

        self.todo_list = QListWidget(self.frame)
        self.todo_list.setObjectName(u"todo_list")

        self.verticalLayout_5.addWidget(self.todo_list)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.daiban)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_3.addWidget(self.comboBox)

        self.addLectures = QPushButton(self.frame_2)
        self.addLectures.setObjectName(u"addLectures")

        self.verticalLayout_3.addWidget(self.addLectures)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_3.addWidget(self.pushButton)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 20))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_5)

        self.title = QLineEdit(self.frame_2)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(0, 30))

        self.verticalLayout_3.addWidget(self.title)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.info = QPlainTextEdit(self.frame_2)
        self.info.setObjectName(u"info")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.info.sizePolicy().hasHeightForWidth())
        self.info.setSizePolicy(sizePolicy1)
        self.info.setMinimumSize(QSize(0, 40))
        self.info.setMaximumSize(QSize(16777215, 120))

        self.verticalLayout_3.addWidget(self.info)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.category = QPlainTextEdit(self.frame_2)
        self.category.setObjectName(u"category")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.category.sizePolicy().hasHeightForWidth())
        self.category.setSizePolicy(sizePolicy2)
        self.category.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_3.addWidget(self.category)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.StartTime = QDateTimeEdit(self.frame_2)
        self.StartTime.setObjectName(u"StartTime")

        self.verticalLayout_3.addWidget(self.StartTime)

        self.EndTime = QDateTimeEdit(self.frame_2)
        self.EndTime.setObjectName(u"EndTime")

        self.verticalLayout_3.addWidget(self.EndTime)

        self.save_button_3 = QPushButton(self.frame_2)
        self.save_button_3.setObjectName(u"save_button_3")

        self.verticalLayout_3.addWidget(self.save_button_3)


        self.horizontalLayout.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.daiban)
        self.calendar = QWidget()
        self.calendar.setObjectName(u"calendar")
        self.verticalLayout_6 = QVBoxLayout(self.calendar)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_10 = QFrame(self.calendar)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy3)
        self.frame_10.setMinimumSize(QSize(0, 60))
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 0, 5, 0)
        self.Date = QFrame(self.frame_10)
        self.Date.setObjectName(u"Date")
        sizePolicy.setHeightForWidth(self.Date.sizePolicy().hasHeightForWidth())
        self.Date.setSizePolicy(sizePolicy)
        self.Date.setMinimumSize(QSize(30, 0))
        self.Date.setFrameShape(QFrame.Shape.NoFrame)
        self.Date.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_3.addWidget(self.Date)

        self.Mon_up = QLabel(self.frame_10)
        self.Mon_up.setObjectName(u"Mon_up")
        self.Mon_up.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.Mon_up)

        self.Tue_up = QLabel(self.frame_10)
        self.Tue_up.setObjectName(u"Tue_up")
        self.Tue_up.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.Tue_up)

        self.Wedn_up = QLabel(self.frame_10)
        self.Wedn_up.setObjectName(u"Wedn_up")
        self.Wedn_up.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.Wedn_up)

        self.Thu_up = QLabel(self.frame_10)
        self.Thu_up.setObjectName(u"Thu_up")
        self.Thu_up.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.Thu_up)

        self.Fri_up = QLabel(self.frame_10)
        self.Fri_up.setObjectName(u"Fri_up")
        self.Fri_up.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.Fri_up)

        self.Sat_up = QLabel(self.frame_10)
        self.Sat_up.setObjectName(u"Sat_up")
        self.Sat_up.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.Sat_up)

        self.Sun_up = QLabel(self.frame_10)
        self.Sun_up.setObjectName(u"Sun_up")
        self.Sun_up.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.Sun_up)


        self.verticalLayout_6.addWidget(self.frame_10)

        self.frame_3 = QFrame(self.calendar)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy4)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 0, 5, 0)
        self.scrollBar = QFrame(self.frame_3)
        self.scrollBar.setObjectName(u"scrollBar")
        sizePolicy.setHeightForWidth(self.scrollBar.sizePolicy().hasHeightForWidth())
        self.scrollBar.setSizePolicy(sizePolicy)
        self.scrollBar.setMinimumSize(QSize(30, 0))
        self.scrollBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.scrollBar.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_4.addWidget(self.scrollBar)

        self.Mon_whole = QFrame(self.frame_3)
        self.Mon_whole.setObjectName(u"Mon_whole")
        self.Mon_whole.setFrameShape(QFrame.Shape.StyledPanel)
        self.Mon_whole.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_4.addWidget(self.Mon_whole)

        self.Tue_whole = QFrame(self.frame_3)
        self.Tue_whole.setObjectName(u"Tue_whole")
        self.Tue_whole.setFrameShape(QFrame.Shape.StyledPanel)
        self.Tue_whole.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_4.addWidget(self.Tue_whole)

        self.Wedn_whole = QFrame(self.frame_3)
        self.Wedn_whole.setObjectName(u"Wedn_whole")
        self.Wedn_whole.setFrameShape(QFrame.Shape.StyledPanel)
        self.Wedn_whole.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_4.addWidget(self.Wedn_whole)

        self.Thu_whole = QFrame(self.frame_3)
        self.Thu_whole.setObjectName(u"Thu_whole")
        self.Thu_whole.setFrameShape(QFrame.Shape.StyledPanel)
        self.Thu_whole.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_4.addWidget(self.Thu_whole)

        self.Fri_whole = QFrame(self.frame_3)
        self.Fri_whole.setObjectName(u"Fri_whole")
        self.Fri_whole.setFrameShape(QFrame.Shape.StyledPanel)
        self.Fri_whole.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_4.addWidget(self.Fri_whole)

        self.Sat_whole = QFrame(self.frame_3)
        self.Sat_whole.setObjectName(u"Sat_whole")
        self.Sat_whole.setFrameShape(QFrame.Shape.StyledPanel)
        self.Sat_whole.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_4.addWidget(self.Sat_whole)

        self.Sun_whole = QFrame(self.frame_3)
        self.Sun_whole.setObjectName(u"Sun_whole")
        self.Sun_whole.setFrameShape(QFrame.Shape.StyledPanel)
        self.Sun_whole.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_4.addWidget(self.Sun_whole)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.scrollArea = QScrollArea(self.calendar)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 641, 1440))
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.Scroll_bar = QFrame(self.scrollAreaWidgetContents)
        self.Scroll_bar.setObjectName(u"Scroll_bar")
        sizePolicy.setHeightForWidth(self.Scroll_bar.sizePolicy().hasHeightForWidth())
        self.Scroll_bar.setSizePolicy(sizePolicy)
        self.Scroll_bar.setMinimumSize(QSize(30, 0))
        self.Scroll_bar.setFrameShape(QFrame.Shape.NoFrame)
        self.Scroll_bar.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.Scroll_bar)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.horizontalLayout_2.addWidget(self.Scroll_bar)

        self.Mon = QFrame(self.scrollAreaWidgetContents)
        self.Mon.setObjectName(u"Mon")
        sizePolicy1.setHeightForWidth(self.Mon.sizePolicy().hasHeightForWidth())
        self.Mon.setSizePolicy(sizePolicy1)
        self.Mon.setMinimumSize(QSize(0, 1440))
        self.Mon.setFrameShape(QFrame.Shape.StyledPanel)
        self.Mon.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.Mon)

        self.Tue = QFrame(self.scrollAreaWidgetContents)
        self.Tue.setObjectName(u"Tue")
        sizePolicy4.setHeightForWidth(self.Tue.sizePolicy().hasHeightForWidth())
        self.Tue.setSizePolicy(sizePolicy4)
        self.Tue.setMinimumSize(QSize(0, 0))
        self.Tue.setFrameShape(QFrame.Shape.StyledPanel)
        self.Tue.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.Tue)

        self.Wedn = QFrame(self.scrollAreaWidgetContents)
        self.Wedn.setObjectName(u"Wedn")
        sizePolicy4.setHeightForWidth(self.Wedn.sizePolicy().hasHeightForWidth())
        self.Wedn.setSizePolicy(sizePolicy4)
        self.Wedn.setMinimumSize(QSize(0, 0))
        self.Wedn.setFrameShape(QFrame.Shape.StyledPanel)
        self.Wedn.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.Wedn)

        self.Thu = QFrame(self.scrollAreaWidgetContents)
        self.Thu.setObjectName(u"Thu")
        sizePolicy4.setHeightForWidth(self.Thu.sizePolicy().hasHeightForWidth())
        self.Thu.setSizePolicy(sizePolicy4)
        self.Thu.setMinimumSize(QSize(0, 0))
        self.Thu.setFrameShape(QFrame.Shape.StyledPanel)
        self.Thu.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.Thu)

        self.Fri = QFrame(self.scrollAreaWidgetContents)
        self.Fri.setObjectName(u"Fri")
        sizePolicy4.setHeightForWidth(self.Fri.sizePolicy().hasHeightForWidth())
        self.Fri.setSizePolicy(sizePolicy4)
        self.Fri.setMinimumSize(QSize(0, 0))
        self.Fri.setFrameShape(QFrame.Shape.StyledPanel)
        self.Fri.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.Fri)

        self.Sat = QFrame(self.scrollAreaWidgetContents)
        self.Sat.setObjectName(u"Sat")
        sizePolicy4.setHeightForWidth(self.Sat.sizePolicy().hasHeightForWidth())
        self.Sat.setSizePolicy(sizePolicy4)
        self.Sat.setMinimumSize(QSize(0, 0))
        self.Sat.setFrameShape(QFrame.Shape.StyledPanel)
        self.Sat.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.Sat)

        self.Sun = QFrame(self.scrollAreaWidgetContents)
        self.Sun.setObjectName(u"Sun")
        sizePolicy4.setHeightForWidth(self.Sun.sizePolicy().hasHeightForWidth())
        self.Sun.setSizePolicy(sizePolicy4)
        self.Sun.setMinimumSize(QSize(0, 0))
        self.Sun.setFrameShape(QFrame.Shape.StyledPanel)
        self.Sun.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.Sun)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_6.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.calendar)

        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(60, 0))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.widget_2.setMinimumSize(QSize(0, 80))
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.widget_3.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.avatar = QPushButton(self.widget_3)
        self.avatar.setObjectName(u"avatar")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.avatar.sizePolicy().hasHeightForWidth())
        self.avatar.setSizePolicy(sizePolicy5)
        self.avatar.setMinimumSize(QSize(40, 80))
        self.avatar.setMaximumSize(QSize(80, 80))

        self.horizontalLayout_5.addWidget(self.avatar)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.username = QLabel(self.widget_2)
        self.username.setObjectName(u"username")
        sizePolicy1.setHeightForWidth(self.username.sizePolicy().hasHeightForWidth())
        self.username.setSizePolicy(sizePolicy1)
        self.username.setMinimumSize(QSize(0, 20))
        self.username.setScaledContents(True)
        self.username.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.username)


        self.verticalLayout.addWidget(self.widget_2)

        self.diary_button = QPushButton(self.widget)
        self.diary_button.setObjectName(u"diary_button")
        sizePolicy1.setHeightForWidth(self.diary_button.sizePolicy().hasHeightForWidth())
        self.diary_button.setSizePolicy(sizePolicy1)
        self.diary_button.setMinimumSize(QSize(0, 60))

        self.verticalLayout.addWidget(self.diary_button)

        self.todo_button = QPushButton(self.widget)
        self.todo_button.setObjectName(u"todo_button")
        self.todo_button.setMinimumSize(QSize(0, 60))

        self.verticalLayout.addWidget(self.todo_button)

        self.calendar_button = QPushButton(self.widget)
        self.calendar_button.setObjectName(u"calendar_button")
        self.calendar_button.setMinimumSize(QSize(0, 60))

        self.verticalLayout.addWidget(self.calendar_button)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 809, 37))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.mon.setText(QCoreApplication.translate("MainWindow", u"Monday", None))
        self.wed.setText(QCoreApplication.translate("MainWindow", u"Wednesday", None))
        self.tue.setText(QCoreApplication.translate("MainWindow", u"Tuesday", None))
        self.thu.setText(QCoreApplication.translate("MainWindow", u"Thursday", None))
        self.fri.setText(QCoreApplication.translate("MainWindow", u"Friday", None))
        self.sat.setText(QCoreApplication.translate("MainWindow", u"Saturday", None))
        self.sun.setText(QCoreApplication.translate("MainWindow", u"Sunday", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"back to today", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Select Date", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"go and see", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"save", None))
        self.produce_report.setText(QCoreApplication.translate("MainWindow", u"See Report", None))
        self.inform_text.setText(QCoreApplication.translate("MainWindow", u"Welcome to diary mode! Write whatever you like!", None))
        self.generate_graph_button.setText(QCoreApplication.translate("MainWindow", u"View statitics from the past seven days", None))
        self.inform_text2.setText(QCoreApplication.translate("MainWindow", u"   No record of rating!", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Write your to-do list! (you can change \"today\" below)", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6570\u5b66\u79d1\u5b66\u5b66\u9662", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u6279\u91cf\u5bfc\u5165\uff08\u5c0f\u5317\u540c\u5b66\uff09", None))

        self.addLectures.setText(QCoreApplication.translate("MainWindow", u"addLectures", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Input events freeeely!", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Start & End", None))
        self.save_button_3.setText(QCoreApplication.translate("MainWindow", u"save", None))
        self.Mon_up.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Tue_up.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Wedn_up.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Thu_up.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Fri_up.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Sat_up.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Sun_up.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.avatar.setText("")
        self.username.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.diary_button.setText(QCoreApplication.translate("MainWindow", u"Diary", None))
        self.todo_button.setText(QCoreApplication.translate("MainWindow", u"To-Do", None))
        self.calendar_button.setText(QCoreApplication.translate("MainWindow", u"Calendar", None))
    # retranslateUi

