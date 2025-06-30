import sys
from PySide6.QtWidgets import QWidget, QTextEdit, QPushButton
from ui_form import Ui_MainWindow
from PySide6.QtCore import QDate
import datetime
import json
import os

DIARY_FILE_PATH = 'diary_data.json'
diary_data = {}

def load_diary_data(user):
    global diary_data
    try:
        if os.path.exists(DIARY_FILE_PATH):
            with open(DIARY_FILE_PATH, 'r') as file:
                all_data = json.load(file)
                diary_data = all_data.get(user, {})
        else:
            diary_data = {}
    except Exception as e:
        print(f"Error loading diary data: {e}")
        diary_data = {}

def save_diary_data(user):
    try:
        all_data = {}
        if os.path.exists(DIARY_FILE_PATH):
            with open(DIARY_FILE_PATH, 'r') as file:
                all_data = json.load(file)
        all_data[user] = diary_data
        with open(DIARY_FILE_PATH, 'w') as file:
            json.dump(all_data, file)
    except Exception as e:
        print(f"Error saving diary data: {e}")

def set_diary_button(window,start_of_week):
    window.monb.setText(f"Monday\n{start_of_week.toString('yyyy-MM-dd')}")
    window.tueb.setText(f"Tuesday\n{start_of_week.addDays(1).toString('yyyy-MM-dd')}")
    window.wedb.setText(f"Wednesday\n{start_of_week.addDays(2).toString('yyyy-MM-dd')}")
    window.thub.setText(f"Thursday\n{start_of_week.addDays(3).toString('yyyy-MM-dd')}")
    window.frib.setText(f"Friday\n{start_of_week.addDays(4).toString('yyyy-MM-dd')}")
    window.satb.setText(f"Saturday\n{start_of_week.addDays(5).toString('yyyy-MM-dd')}")
    window.sunb.setText(f"Sunday\n{start_of_week.addDays(6).toString('yyyy-MM-dd')}")
    button_height = 60
    window.monb.setStyleSheet(f"height: {button_height}px;")
    window.tueb.setStyleSheet(f"height: {button_height}px;")
    window.wedb.setStyleSheet(f"height: {button_height}px;")
    window.thub.setStyleSheet(f"height: {button_height}px;")
    window.frib.setStyleSheet(f"height: {button_height}px;")
    window.satb.setStyleSheet(f"height: {button_height}px;")
    window.sunb.setStyleSheet(f"height: {button_height}px;")

def set_week_dates(window):
    today = QDate.currentDate()
    start_of_week = today.addDays(-today.dayOfWeek() + 1)
    set_diary_button(window,start_of_week)

#add
def print_score_info(window, date_str):
    file_path = os.path.join(os.path.dirname(__file__), 'emotion_scores.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            emotion_score_dict = json.load(f)
    else:
        print("not found,called by diary")
        window.score_text.setText("No record of rating, see one NOW!")
        return

    user = window.user
    user_emotion_score = emotion_score_dict.get(user, {})
    if date_str in user_emotion_score:  # 先检查记录是否存在
        score, timestamp = user_emotion_score[date_str]
        window.score_text.setText(f"上次评分时间:{timestamp}, emotion rating:{score}")
    else:
        window.score_text.setText("No record of rating, see one NOW!")

def show_diary(day, window, date_str):
    #add
    print_score_info(window,date_str)

    formatted_date = date_str
    weekday_name = QDate.fromString(date_str, "yyyy-MM-dd").toString("dddd")  #获取星期几
    head_text = f"Today is {formatted_date} ({weekday_name})"
    window.current_date = QDate.fromString(date_str, "yyyy-MM-dd")

    diary_text = diary_data.get(formatted_date, "")

    if not diary_text:
        diary_text = "No diary for today, write one now!"

    window.input_text.setText(diary_text)
    window.inform_text.setText(head_text)

def save_diary(window, date_str):
    user = window.user
    formatted_date = date_str
    diary_content = window.input_text.toPlainText()
    window.current_date = QDate.fromString(date_str, "yyyy-MM-dd")

    if not diary_content.strip():
        window.inform_text.setText("No diary for today, write one now!")
    else:
        diary_data[formatted_date] = diary_content
        save_diary_data(user)
        window.inform_text.setText(f"Your diary for {formatted_date} has been saved!")

def mode_selected_date(window,selected_date):#selected_date-->QDate
    day_of_week = selected_date.dayOfWeek()
    start_of_week = selected_date.addDays(-day_of_week + 1)
    set_diary_button(window,start_of_week)

def mode_now(window):
    today = QDate.currentDate()
    day_ofweek=today.dayOfWeek()
    start_ofweek=today.addDays(-day_ofweek + 1)
    set_diary_button(window,start_ofweek)
