# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
import datetime

class ShowCalendarDate:
    def __init__(self):
        self.current_date = datetime.datetime.now()

    def get_week_dates(self):
        weekday = self.current_date.weekday()
        start_of_week = self.current_date - datetime.timedelta(days=weekday)
        week_dates = []
        for i in range(7):
            day = start_of_week + datetime.timedelta(days=i)
            week_dates.append(day)
        return week_dates

    def get_weekday_names(self):
        return ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    def get_formatted_week(self):
        week_dates = self.get_week_dates()
        weekday_names = self.get_weekday_names()
        return [f"{date.strftime('%Y-%m-%d')} - {weekday_names[i]}"
                for i, date in enumerate(week_dates)]
