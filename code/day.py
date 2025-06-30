from calendar_event import CalendarEvent

class Day:
    def __init__(self, date_str):
        self.date = date_str  # "2025-06-01"
        self.events = []

    def add_event(self, event: CalendarEvent):
        self.events.append(event)

    def remove_event(self, title):
        title = title.strip().lower()
        before = len(self.events)
        self.events = [e for e in self.events if e.title.strip().lower() != title]
        return len(self.events) < before  # 只要有删，就返回 True

    def list_events(self):
        return sorted(self.events,key=lambda e:e.time)
