from datetime import datetime

class CalendarEvent:
    def __init__(self, title, time_str, end_time, category="默认", note="", done=False):
        self.title = title  # 事件标题
        self.time = time_str  # "2025-06-01 15:00" 等字符串
        self.category = category
        self.note = note
        self.done = done
        self.end_time = end_time

    def __repr__(self):
        return f"[{'✔' if self.done else '✘'}] {self.time} - {self.title} ({self.category})"
