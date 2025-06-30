import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QMessageBox, QPushButton, QColorDialog
from PySide6.QtCore import QDateTime, QDate, QTime
from PySide6.QtGui import QPainter, QPen, QPixmap, QIcon
from AvatarDialog import AvatarDialog
from ui_form import Ui_MainWindow
from calendar_date import ShowCalendarDate
from diary import set_week_dates, show_diary, save_diary, load_diary_data,print_score_info,mode_selected_date,mode_now,set_diary_button
from emo_eval import emo_eval
from datetime import datetime
from departments_lecture import sms
from calendar_controller import CalendarController
from zoneinfo import ZoneInfo
from calendar_date import ShowCalendarDate
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QGraphicsScene, QGraphicsView
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from robot_for_xiaobei import xiaobei
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
import os
import matplotlib.patches as mpatches
import json
import re
from ai_input_dialog import AIInputDialog
from event_eval import event_eval  # 你已有的AI解析函数
now = datetime.now(ZoneInfo("Asia/Shanghai"))

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.user = ""

        #change
        self.calendar = CalendarController(f"calendar_data_{self.user}.json")

        self.current_date = QDate.currentDate() #默认为当前日期
        weekday=self.current_date.dayOfWeek()
        start_of_week = self.current_date.addDays(-weekday + 1)
        week_dates = []
        for i in range(7):
            day = start_of_week.addDays(i)
            week_dates.append(day.toString("yyyy-MM-dd"))  #-->string

        self.x=self.current_date.toString("yyyy-MM-dd") #string  记录选择的日期/现实世界的当前日期
        self.emotion_score={}
        self.load_emotion_scores()
        self.score_text=self.ui.inform_text2
        self.ui.generate_graph_button.clicked.connect(lambda:self.plot_emotion_scores(self.x))
        self.past_button=self.ui.pushButton_2
        self.now_button=self.ui.pushButton_3
        self.past_button.clicked.connect(self.goto_past)
        self.now_button.clicked.connect(self.goto_now)
        self.report = self.ui.ai_analyse
        self.report.setText("See ai analysis for your diary HERE!")#清空ai输出，显示提示语
        self.ui.inform_text2.setText("Click 'See Report' to see your emotion rating!")#初始化打分提示词
        #初始化选择日期栏目，默认这个月的第一天
        self.select_date=self.ui.selectDate
        first_day_of_month = QDate(self.current_date.year(), self.current_date.month(), 1)
        self.select_date.setDate(first_day_of_month)

        self.stacked_widget = self.ui.stackedWidget
        self.page1 = self.ui.riji
        self.page2 = self.ui.daiban
        self.page3 = self.ui.calendar
        self.diary_button = self.ui.diary_button
        self.todo_button = self.ui.todo_button
        self.diary_button.clicked.connect(self.show_page1)
        self.todo_button.clicked.connect(self.show_page2)

        self.monb = self.ui.mon
        self.tueb = self.ui.tue
        self.wedb = self.ui.wed
        self.thub = self.ui.thu
        self.frib = self.ui.fri
        self.satb = self.ui.sat
        self.sunb = self.ui.sun
        self.save_button = self.ui.save_button
        self.input_text = self.ui.input_text
        self.inform_text = self.ui.inform_text
        set_week_dates(self)

        self.ui.avatar.clicked.connect(self.set_avatar)
        #change 6.28
        self.monb.clicked.connect(lambda: show_diary("Monday", self, week_dates[0]),print_score_info(self,week_dates[0]))
        self.tueb.clicked.connect(lambda: show_diary("Tuesday", self,  week_dates[1]),print_score_info(self,week_dates[1]))
        self.wedb.clicked.connect(lambda: show_diary("Wednesday", self, week_dates[2]),print_score_info(self,week_dates[2]))
        self.thub.clicked.connect(lambda: show_diary("Thursday", self,week_dates[3]),print_score_info(self,week_dates[3]))
        self.frib.clicked.connect(lambda: show_diary("Friday", self, week_dates[4]),print_score_info(self,week_dates[4]))
        self.satb.clicked.connect(lambda: show_diary("Saturday", self, week_dates[5]),print_score_info(self,week_dates[5]))
        self.sunb.clicked.connect(lambda: show_diary("Sunday", self, week_dates[6]),print_score_info(self,week_dates[6]))
        self.save_button.clicked.connect(lambda: save_diary(self, self.current_date.toString("yyyy-MM-dd")))

        self.ui.calendar_button.clicked.connect(self.show_page3)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.produce_report.clicked.connect(self.generate_report)
        self.ui.save_button_3.clicked.connect(self.makeNewEvent)
        self.ui.addLectures.clicked.connect(self.addlectures)
        self.evaluator = emo_eval()
        self.ui.today.dateChanged.connect(self.refresh_list)

        #self.ui.category.addItem("默认", -1)
        self.dept_sms = sms()
        self.dept_xiaobei = xiaobei()

        self.ui.todo_list.itemDoubleClicked.connect(self.toggle_event_done)

        self.ui.pushButton.clicked.connect(self.open_ai_input_dialog)


        def draw_time_axis_on_scroll(scroll_area, block_height=30):
            frame = scroll_area.widget()
            if frame is None:
                raise ValueError("scroll_area.widget() is None — 请先设置 setWidget()")
            def paintEvent(event):
                QWidget.paintEvent(frame, event)
                painter = QPainter(frame)
                pen = QPen(Qt.gray)
                pen.setWidth(1)
                painter.setPen(pen)
                for i in range(25):
                    y = i * block_height
                    painter.drawLine(5, y, frame.width()-5, y)
                # 可选：加时间文字
                painter.setPen(Qt.darkGray)
                for i in range(24):
                    painter.drawText(5, i * block_height + 15, f"{i:02d}:00")
                painter.end()
            frame.setMinimumHeight(block_height * 24)
            frame.paintEvent = paintEvent
            frame.update()

        draw_time_axis_on_scroll(self.ui.scrollArea, 60)

        '''
        self.setStyleSheet("""
            /* 整体背景与字体设置 */
            QWidget {
                background-color: #FFF8F2;   /* 整体背景色：浅米色 */
                font-family: 'Arial';        /* 全局字体 */
                font-size: 12px;             /* 字体大小 */
                font-weight: bold;
            }

            /* 所有 QPushButton 的基础样式 */
            QPushButton {
                background-color: #FAD59A;   /* 按钮背景色：棕色（奶油感） */
                border: 1px solid #dddddd;   /* 按钮边框色：同上 */
                border-radius: 12px;         /* 按钮圆角：越大越圆 */
                padding: 6px 6px;          /* 按钮内边距 */
            }

            /* 鼠标悬停时的按钮颜色变化 */
            QPushButton:hover {
                background-color: #e8e8e8;   /* 按钮悬停时的颜色：略深的灰白 */
            }

            /* 鼠标按下时的按钮颜色变化 */
            QPushButton:pressed {
                background-color: #dcdcdc;   /* 按钮按下时颜色：更深一点的灰白 */
            }

            /* 文本输入类控件样式（输入框、多行编辑器、浏览器） */
            QLineEdit, QPlainTextEdit, QTextEdit, QTextBrowser {
                background-color: #FFF8F2;   /* 输入框背景色：非常淡的灰白 */
                border: 1px solid #dddddd;   /* 输入框边框色：浅灰 */
                border-radius: 8px;          /* 输入框圆角 */
                padding: 5px;                /* 内边距 */
            }

            /* 标签文字颜色（如“Username”、“Title”等） */
            QLabel {
                color: #333333;              /* 标签文字颜色：深灰黑，更柔和 */
            }

            /* 待办事项列表样式 */
            QListWidget {
                background-color: #FFF8F2;   /* 列表背景色：极淡灰白 */
                border: 1px solid #dddddd;   /* 边框颜色：浅灰 */
                border-radius: 8px;          /* 列表圆角 */
            }

            /* 日期与时间编辑器样式 */
            QDateEdit, QDateTimeEdit {
                background-color: #FFF8F2;   /* 日期时间控件背景：纯白 */
                border: 1px solid #cccccc;   /* 边框颜色：偏浅灰 */
                border-radius: 6px;          /* 圆角稍小一点 */
                padding: 4px;                /* 内边距 */
            }

            /* 页面切换容器（StackedWidget）背景 */
            QStackedWidget {
                background-color: #FFF8F2;   /* 页面背景色：纯白 */
            }
        """)
        '''

        class CalDayView:
            def __init__(self, text, no_time, has_time):
                self.show_date = text
                self.no_time = no_time
                self.has_time = has_time
                self.eventWidgets = []

            def clearList(self):
                self.eventWidgets.clear()
                for child in self.show_date.findChildren(QWidget):
                    child.setText()
                for fr in self.no_time.findChildren(QWidget):
                    fr.setParent(None)
                for fr in self.has_time.findChildren(QWidget):
                    fr.setParent(None)
                self.no_time.update()
                self.has_time.update()

            @staticmethod
            def calculateY(time_str):
                try:
                    hr, min = list(map(int, time_str.split(":")))
                    return hr * 60 + min
                except:
                    return -1
            def setDate(self, date_str):
                q_date = QDate.fromString(date_str, "yyyy-MM-dd")
                weekDay = q_date.dayOfWeek()
                week_map = {
                    1: "星期一",
                    2: "星期二",
                    3: "星期三",
                    4: "星期四",
                    5: "星期五",
                    6: "星期六",
                    7: "星期日"
                }
                self.show_date.setText(date_str + '\n' + week_map[weekDay])
            def addEvent(self, event):
                eventTitle = event.title
                startTime = event.time[-5:]
                endTime = event.end_time
                category = event.category

                up = CalDayView.calculateY(startTime)
                down = CalDayView.calculateY(endTime)
                if up == -1 and down == -1:
                    return
                if down == -1:
                    down = up + 60

                # 初始化事件列表
                if not hasattr(self, "_pending_events"):
                    self._pending_events = []

                self._pending_events.append({
                    "event": event,
                    "start": up,
                    "end": down,
                    "title": eventTitle,
                    "category": category
                })
            def finalizeLayout(self, w):
                events = getattr(self, "_pending_events", [])
                events.sort(key=lambda e: e['start'])

                # 分组重叠事件
                groups = []
                group = []
                for e in events:
                    if not group:
                        group.append(e)
                    else:
                        last_end = max(x['end'] for x in group)
                        if e['start'] < last_end:
                            group.append(e)
                        else:
                            groups.append(group)
                            group = [e]
                if group:
                    groups.append(group)
                self.eventWidgets.clear()
                for group in groups:
                    columns = []
                    for e in group:
                        for i, col in enumerate(columns):
                            if e['start'] >= col[-1]['end']:
                                col.append(e)
                                e['col'] = i
                                break
                        else:
                            e['col'] = len(columns)
                            columns.append([e])

                    total_cols = len(columns)
                    for e in group:
                        col_width = w / total_cols
                        x = e['col'] * col_width
                        y = e['start']
                        height = e['end'] - e['start']

                        btn = QPushButton(self.has_time)
                        btn.setGeometry(x, y, col_width, height)
                        btn.setStyleSheet("""
                            QPushButton {
                                background-color: rgba(255, 255, 255, 150);
                                border: 1px solid #aaa;
                                border-radius: 0px;
                                text-align: top center;
                                padding: 0px;  /* 去掉内边距 */
                                margin: 0px;   /* 防止外间距 */
                                font-size: 10pt;
                                color: #222;
                            }
                            QPushButton:hover {
                                background-color: rgba(135, 206, 250, 150);
                            }
                        """)
                        tooltip = (
                            f"{e['title']}\n类别：{e['category']}\n"
                            f"开始时间：{int(e['start']//60):02}:{int(e['start']%60):02}\n"
                            f"结束时间：{int(e['end']//60):02}:{int(e['end']%60):02}"
                        )
                        btn.setToolTip(tooltip)
                        btn.show()
                        self.eventWidgets.append(btn)
                self._pending_events.clear()
        self.calendarFrames = []
        text = [self.ui.Mon_up, self.ui.Tue_up, self.ui.Wedn_up, self.ui.Thu_up, self.ui.Fri_up, self.ui.Sat_up, self.ui.Sun_up]
        no_time = [self.ui.Mon_whole, self.ui.Tue_whole, self.ui.Wedn_whole, self.ui.Thu_whole, self.ui.Fri_whole, self.ui.Sat_whole, self.ui.Sun_whole]
        has_time = [self.ui.Mon, self.ui.Tue, self.ui.Wedn, self.ui.Thu, self.ui.Fri, self.ui.Sat, self.ui.Sun]

        for t, nt, ht in zip(text, no_time, has_time):
            self.calendarFrames.append(CalDayView(t, nt, ht))

    #change**
    def setuser(self, usr):
        self.ui.username.setText(usr)
        self.user = usr
        load_diary_data(self.user) #add
        self.calendar = CalendarController(f"calendar_data_{self.user}.json")
        set_week_dates(self) #add

    def change_date(self, date_str):
        self.current_date = QDate.fromString(date_str, "yyyy-MM-dd")
        self.show_diary(date_str)

    def show_page1(self):
        self.stacked_widget.setCurrentWidget(self.page1)
        self.ui.inform_text2.setText("Click 'See Report' to see your emotion rating!")
    def show_page2(self):
        self.stacked_widget.setCurrentWidget(self.page2)
        self.ui.today.setDateTime(QDateTime.currentDateTime())
        self.ui.StartTime.setDateTime(QDateTime.currentDateTime())
        self.ui.EndTime.setDateTime(QDateTime.currentDateTime())
        self.refresh_list()
    def addCategory(self):
        selection = self.ui.category.currentText()
        data = self.ui.category.currentData()
        if data == -1:
            self.newCategory()

    def newCategory(self):
        color = QColorDialog()
        color.show()
        #color.

    def show_page3(self):
        self.loadCalendar()
        self.stacked_widget.setCurrentWidget(self.page3)


    def makeNewEvent(self):
        start = convertTime(self.ui.StartTime.dateTime()).strftime("%H:%M")
        end = convertTime(self.ui.EndTime.dateTime()).strftime("%H:%M")
        date = convertTime(self.ui.StartTime.dateTime()).strftime("%Y-%m-%d")
        info = self.ui.info.toPlainText()
        title = self.ui.title.text()
        category = self.ui.category.toPlainText()
        flag, msg = self.calendar.add_event(date, title, start, end, category, info)
        if flag == False:
            QMessageBox.critical(msg)
        self.refresh_list()

    def refresh_list(self):
        day_today = self.ui.today.date()
        events = self.calendar.get_events(day_today.toString("yyyy-MM-dd"))
        self.ui.todo_list.clear()
        self.currentEventInfo = []
        for event in events:
            self.ui.todo_list.addItem(repr(event))
            self.currentEventInfo.append(event)
        #self.ui.todo_list.addItem("123")

    def addlectures(self):
        choice = self.ui.comboBox.currentIndex()
        if choice == 0:
            eventWithDate = self.dept_sms.create_events()
            for event in eventWithDate:
                flag, msg = self.calendar.add_event(*event)
        if choice == 1:
            eventWithDate = self.dept_xiaobei.create_events()
            for event in eventWithDate:
                flag, msg = self.calendar.add_event(*event)

    def loadEventsOfWeek(self, monday):
        events_dict = dict()
        currDay = monday
        for _ in range(7):
            date_str = currDay.toString("yyyy-MM-dd")
            today_events = self.calendar.get_events(date_str)
            events_dict[date_str] = today_events
            currDay = currDay.addDays(1)
        return events_dict

    def loadCalendar(self, currDay = QDate.currentDate()):
            weekday = currDay.dayOfWeek()
            # 减去 weekday - 1 天，得到本周的星期一
            monday = currDay.addDays(1 - weekday)
            events_dict = self.loadEventsOfWeek(monday)
            for i in range(7):
                date = list(events_dict.keys())[i]
                self.calendarFrames[i].clearList()
                self.calendarFrames[i].setDate(date)
                event_lst = events_dict[date]
                for event in event_lst:
                    self.calendarFrames[i].addEvent(event)
                try:
                    eachW = (self.ui.scrollArea.width() - 10) // 7 - 3
                    self.calendarFrames[i].finalizeLayout(eachW)
                except:
                    continue
    def toggle_event_done(self, item):
            # 1. 获取当前日期字符串
            date_str = self.ui.today.date().toString("yyyy-MM-dd")

            # 2. 解析事件标题
            content = item.text().strip()
            # 正则：匹配形如 "[✔] 09:20 - 吃饭 (分类)" 或 "[✘] 09:20 - 吃饭"
            match = re.match(r"\[\s*[✔✘]\s*\]\s*(\d{2}:\d{2})\s*-\s*(.+?)(?:\s*\(.*\))?$", content)
            if not match:
                QMessageBox.warning(self, "解析失败", "无法识别事件格式")
                return

            time_str = match.group(1)       # 例如 "09:20"
            title = match.group(2).strip()  # 去掉括号内容后是标题


            # 3. 标记完成
            ok, msg = self.calendar.toggle_done(date_str, title, time_str)
            if ok:
                self.refresh_list()
            else:
                QMessageBox.warning(self, "标记失败", msg)
    def calender_clicked(self, event):
        pass

    def goto_past(self):
        self.report.setText("See ai analysis for your diary HERE!")#清空ai输出，显示提示语
        selected_date=self.select_date.date()
        dayof_week = selected_date.dayOfWeek()
        startof_week = selected_date.addDays(-dayof_week + 1)
        week_dates = []
        for i in range(7):
            week_dates.append(startof_week.addDays(i).toString("yyyy-MM-dd"))
        self.monb.clicked.connect(lambda: show_diary("Monday", self, week_dates[0]),print_score_info(self,week_dates[0]))
        self.tueb.clicked.connect(lambda: show_diary("Tuesday", self,  week_dates[1]),print_score_info(self,week_dates[1]))
        self.wedb.clicked.connect(lambda: show_diary("Wednesday", self, week_dates[2]),print_score_info(self,week_dates[2]))
        self.thub.clicked.connect(lambda: show_diary("Thursday", self,week_dates[3]),print_score_info(self,week_dates[3]))
        self.frib.clicked.connect(lambda: show_diary("Friday", self, week_dates[4]),print_score_info(self,week_dates[4]))
        self.satb.clicked.connect(lambda: show_diary("Saturday", self, week_dates[5]),print_score_info(self,week_dates[5]))
        self.sunb.clicked.connect(lambda: show_diary("Sunday", self, week_dates[6]),print_score_info(self,week_dates[6]))
        selected_date_str = selected_date.toString("yyyy-MM-dd")
        self.x=selected_date_str
        mode_selected_date(self,selected_date)
        show_diary(selected_date.toString("dddd"), self, self.x)


    def goto_now(self):
        self.report.setText("See ai analysis for your diary HERE!")#清空ai输出，显示提示语
        today = QDate.currentDate()
        self.x=today.toString("yyyy-MM-dd")
        weekday=today.dayOfWeek()
        start_of_week = today.addDays(-weekday + 1)
        week_dates = []
        for i in range(7):
            day = start_of_week.addDays(i)
            week_dates.append(day.toString("yyyy-MM-dd"))  #-->string
        self.monb.clicked.connect(lambda: show_diary("Monday", self, week_dates[0]),print_score_info(self,week_dates[0]))
        self.tueb.clicked.connect(lambda: show_diary("Tuesday", self,  week_dates[1]),print_score_info(self,week_dates[1]))
        self.wedb.clicked.connect(lambda: show_diary("Wednesday", self, week_dates[2]),print_score_info(self,week_dates[2]))
        self.thub.clicked.connect(lambda: show_diary("Thursday", self,week_dates[3]),print_score_info(self,week_dates[3]))
        self.frib.clicked.connect(lambda: show_diary("Friday", self, week_dates[4]),print_score_info(self,week_dates[4]))
        self.satb.clicked.connect(lambda: show_diary("Saturday", self, week_dates[5]),print_score_info(self,week_dates[5]))
        self.sunb.clicked.connect(lambda: show_diary("Sunday", self, week_dates[6]),print_score_info(self,week_dates[6]))
        mode_now(self)
        show_diary(today.toString("dddd"), self, self.x)

    def generate_report(self):
        text = self.ui.input_text.toPlainText()
        score, feedback = self.evaluator.eval(text)
        save_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        this_day = self.current_date.toString("yyyy-MM-dd")

        # 保存用户的情绪评分（修改为多用户结构）
        user = self.user
        file_path = os.path.join(os.path.dirname(__file__), 'emotion_scores.json')
        try:
            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    emotion_score_dict = json.load(f)
            else:
                emotion_score_dict = {}

            if user not in emotion_score_dict:
                emotion_score_dict[user] = {}
            emotion_score_dict[user][this_day] = [score, save_time]
            with open(file_path, 'w') as f:
                json.dump(emotion_score_dict, f)
        except Exception as e:
            print(f"Error saving emotion score: {e}")
        self.ui.ai_analyse.setText(f"Score: {score}\nFeedback: {feedback}")
        self.score_text.setText(f"上次评分时间:{save_time}, emotion rating:{score}")
    def score_renew_info(self,date_str):
            self.load_emotion_scores()
            if date_str in self.emotion_score:
                self.score_text.setText(f"上次评分时间:{self.emotion_score[date_str][1]}, \
                                                    emotion rating:{self.emotion_score[date_str][0]}")
            else:
                self.score_text.setText("No record of rating now")

    def load_emotion_scores(self):
        user = self.user
        file_path = os.path.join(os.path.dirname(__file__), 'emotion_scores.json')
        try:
            if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                with open(file_path, 'r') as f:
                    emotion_score_dict = json.load(f)
                    self.emotion_score = emotion_score_dict.get(user, {})
            else:
                print("文件为空或不存在，正在创建新文件")
                self.emotion_score = {}
                with open(file_path, 'w') as f:
                    json.dump({user: self.emotion_score}, f)
        except Exception as e:
            print(f"Error loading emotion scores: {e}")
            self.emotion_score = {}

    def save_emotion_scores(self):
        user = self.user
        file_path = os.path.join(os.path.dirname(__file__), 'emotion_scores.json')
        try:
            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    emotion_score_dict = json.load(f)
            else:
                emotion_score_dict = {}
            emotion_score_dict[user] = self.emotion_score.get(user, {})
            with open(file_path, 'w') as f:
                json.dump(emotion_score_dict, f)
        except Exception as e:
            print(f"Error saving emotion scores: {e}")
    def plot_emotion_scores(self, dateString):
        rainbow_cmap = LinearSegmentedColormap.from_list(
            "rainbow_custom",
            ["#ff007a", "#ffcc00", "#00e0ff", "#8d00ff", "#ff007a"]
        )

        start_date = QDate.fromString(dateString, "yyyy-MM-dd")
        dates = []
        scores = []
        self.load_emotion_scores()
        for i in range(7):
            day = start_date.addDays(-i)
            date_str = day.toString("yyyy-MM-dd")
            dates.append(date_str)
            if date_str in self.emotion_score:
                scores.append(self.emotion_score[date_str][0])
            else:
                scores.append("No Record")

        dates = dates[::-1]
        scores = scores[::-1]

        fig, ax = plt.subplots(figsize=(10, 6))

        for i, (label, date_str) in enumerate(zip(scores, dates)):
            if label == "No Record":
                ax.bar(i, 0, color="white", width=0.8)
                ax.text(i, 2, "No Record", ha='center', va='bottom', color='gray', fontsize=9)
                continue

            if label >= 90:
                grad_steps = 100
                for j in range(grad_steps):
                    frac = j / grad_steps
                    height = label / grad_steps
                    bottom = frac * label
                    color = rainbow_cmap(frac)
                    ax.bar(i, height, bottom=bottom, color=color, width=0.8)
            else:
                if label >= 70:
                    color = "green"
                elif label >= 50:
                    color = "yellow"
                elif label >= 25:
                    color = "orange"
                else:
                    color = "red"
                ax.bar(i, label, width=0.8, color=color)

            ax.text(i, label + 1, f"{label:.1f}", ha='center', va='bottom', fontsize=9)

        ax.set_ylim(0, 105)
        ax.set_ylabel("Emotion Score")
        ax.set_title(f"Emotion Detection Score for the Past 7-days up to {start_date.toString('yyyy-MM-dd')}")
        ax.set_xticks(np.arange(len(dates)))
        ax.set_xticklabels(dates, rotation=45, ha="right")

        legend_patches = [
            mpatches.Patch(color='#8d00ff', label='90+ (Rainbow Gradient)'),
            mpatches.Patch(color='green', label='70–90'),
            mpatches.Patch(color='yellow', label='50–70'),
            mpatches.Patch(color='orange', label='25–50'),
            mpatches.Patch(color='red', label='0–25'),
        ]
        ax.legend(handles=legend_patches)

        plt.tight_layout()
        plt.show()

    def set_avatar(self):
        avatarDialog = AvatarDialog()
        avatarDialog.exec()
        filePos = avatarDialog.avatarSelected
        pixmap = QPixmap(filePos)
        self.ui.avatar.setIcon(QIcon(pixmap))
        self.ui.avatar.setIconSize(self.ui.avatar.size())
        self.ui.avatar.setStyleSheet("""
        QPushButton {
            border: none;
        }
        QPushButton:pressed {
            background-color: rgba(0, 0, 0, 30);
        }
        """)

#change**
    def open_ai_input_dialog(self):
            dialog = AIInputDialog(self)
            if dialog.exec():  # 如果点击“确定”
                user_input = dialog.get_input_text()
                if not user_input.strip():
                    QMessageBox.warning(self, "提示", "请输入事件描述")
                    return
                try:
                    result = event_eval().eval(user_input)


                    self.ui.title.setText(result.get("title", ""))
                    self.ui.info.setPlainText(result.get("info", ""))
                    self.ui.category.setPlainText(result.get("category", ""))

                    from PySide6.QtCore import QDateTime
                    fmt = "yyyy-MM-dd HH:mm"
                    start = QDateTime.fromString(result.get("StartTime", ""), fmt)
                    end = QDateTime.fromString(result.get("EndTime", ""), fmt)
                    self.ui.StartTime.setDateTime(start)
                    self.ui.EndTime.setDateTime(end)
                    QMessageBox.information(self, "成功", "AI事件解析成功，信息已填入")
                except Exception as e:
                    print(e)
                    QMessageBox.warning(self, "识别失败", str(e))

def convertTime(qt_date):
    py_dt = datetime(
        year=qt_date.date().year(),
        month=qt_date.date().month(),
        day=qt_date.date().day(),
        hour=qt_date.time().hour(),
        minute=qt_date.time().minute(),
        second=qt_date.time().second()
    )
    return py_dt
