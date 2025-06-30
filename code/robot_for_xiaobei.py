#date_str, title, start_time, end_time="", category="默认", note=""
from bs4 import BeautifulSoup
import requests
from datetime import *
from zoneinfo import ZoneInfo
import json

now = datetime.now(ZoneInfo("Asia/Shanghai"))

class departmentsCrawler:
    headers_init = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' +
                  '(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }
    def __init__(self, dep = "元培学院", headers = headers_init):
        self.dep = dep
        self.events = []
        self.headers = headers

    def create_events(self):
        pass

class xiaobei(departmentsCrawler):
    def create_events(self):
        self.events.clear()
        events_uncleaned = self.fetch_info_all() #TODO:如何翻好几页
        #{"title":title, "start":start, "end":end, "lecturer":lecturer, "info_page":info_page}
        for event in events_uncleaned['activity']:
            dt_raw = event['start_time']
            dt = datetime.strptime(dt_raw, "%a, %d %b %Y %H:%M:%S GMT")
            date_str, time_str = dt.strftime("%Y-%m-%d %H:%M").split()
            date_ = date_str
            title = event["event_name"]
            category = "活动-小北同学"
            note = f"举办单位：{ event['event_organizer'] } ，详情见{event['url']}"
            full_event = [date_,title,time_str,'',category, note]
            self.events.append(full_event)
        return self.events

    def fetch_info_all(self, page = 1):
        today = datetime.combine(datetime.today().date(), time())
        url = "https://xiaobei.pku.edu.cn/lecture"
        lec_info_all = self.fetch_info(url, today)
        return lec_info_all

    def fetch_info(self, url, today):
        params = {
            "event_type": "lecture",
            "offset": 0,
            "limit": 100
        }
        res = requests.get('https://xiaobei.pku.edu.cn/api/api_activity', params = params)
        js = json.loads(res.text)
        return js

xb = xiaobei()
xb.create_events()
