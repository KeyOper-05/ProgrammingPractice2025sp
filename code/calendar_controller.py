from day import Day
from calendar_event import CalendarEvent
import json
import os
import re
from datetime import datetime

def is_valid_time_format(t):
    return re.match(r'^([01]\d|2[0-3]):[0-5]\d$', t) is not None

class CalendarController:
    def __init__(self, save_path="calendar_data.json"):
        self.days = {}  # date_str -> Day 对象
        self.save_path = save_path
        self.load_from_file()
        self.categories = []

    def add_event(self, date_str, title, start_time, end_time="", category="默认", note=""):
        if not title or not is_valid_time_format(start_time):
            return False, "标题或开始时间格式不正确"
        if end_time and not is_valid_time_format(end_time):
            return False, "结束时间格式不正确"
        event = CalendarEvent(title.strip(), start_time.strip(), end_time.strip(), category.strip(), note.strip())
        if date_str not in self.days:
            self.days[date_str] = Day(date_str)
        self.days[date_str].add_event(event)
        self.save_to_file()
        if category not in self.categories:
            self.categories.append(category)
        return True, "事件添加成功"

    def remove_event(self, date_str, title):
        if date_str in self.days:
            success = self.days[date_str].remove_event(title)
            if success:
                self.save_to_file()
                return True, "事件已删除"
        return False, "事件不存在"

    def mark_done(self, date_str, title):
        if date_str in self.days:
            for e in self.days[date_str].events:
                if e.title.strip().lower() == title.strip().lower():
                    e.done = True
                    self.save_to_file()
                    return True, "已标记为完成"
        return False, "未找到事件"

    def get_events(self, date_str):
        if date_str in self.days:
            return self.days[date_str].list_events()
        else:
            return []

    def save_to_file(self):
        data = {}
        for date, day in self.days.items():
            data[date] = []
            for e in day.events:
                data[date].append({
                    "title": e.title,
                    "time": e.time,
                    "end_time": e.end_time,
                    "category": e.category,
                    "note": e.note,
                    "done": e.done
                })
        with open(self.save_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load_from_file(self):
        if not os.path.exists(self.save_path):
            return
        with open(self.save_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.days = {}
        for date, events in data.items():
            day = Day(date)
            for e in events:
                event = CalendarEvent(
                    e["title"], e["time"], e.get("end_time", ""),
                    e.get("category", "默认"), e.get("note", ""), e.get("done", False)
                )
                day.add_event(event)
            self.days[date] = day

#add
    def toggle_done(self, date_str, title, time_str=None):
            if date_str not in self.days:
                return False, "找不到日期"
            for event in self.days[date_str].events:
                if event.title == title and (time_str is None or event.time == time_str):
                    event.done = not event.done
                    self.save_to_file()
                    return True, "状态已更新"
            return False, "找不到匹配的事件"
