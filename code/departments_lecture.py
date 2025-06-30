from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime, time
from calendar_event import CalendarEvent
from zoneinfo import ZoneInfo
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


class sms(departmentsCrawler):
    def __init__(self):
        super().__init__(dep = "数学科学学院")
    def create_events(self):
        self.events.clear()
        events_uncleaned = self.fetch_info_all(page = 10) #TODO:如何翻好几页
        #{"title":title, "start":start, "end":end, "lecturer":lecturer, "info_page":info_page}
        for event in events_uncleaned:
            date = event["date"]
            title = event["title"]
            time_str = event["start"]
            category = "讲座与报告-数学科学学院"
            note = f"主讲人：{ event['lecturer'] } ，详情见{event['info_page']}"
            end_time = event["end"]
            full_event = [date,title,time_str,end_time,category, note]
            self.events.append(full_event)
        return self.events

    def fetch_info_all(self, page = 1):
        today = datetime.combine(datetime.today().date(), time())
        url = "https://www.math.pku.edu.cn/kxyj/xsbg/tlb/index.htm"
        url_base = "https://www.math.pku.edu.cn/kxyj/xsbg/tlb/index"
        lec_info_all = self.fetch_info(url, today)
        if page != 1:
            urls = [url_base + str(num_page) + ".htm" for num_page in range(1,page - 1)]
            for url in urls:
                new_info = self.fetch_info(url, today)
                if new_info:
                    lec_info_all += new_info
                else:
                    break
        return lec_info_all

    def fetch_info(self, url, today):
        res = requests.get(url, headers=self.headers, verify=False)
        web = BeautifulSoup(res.text,'lxml')
        list = web.find('ul',class_="scholarsList")
        lec_list = list.find_all('li')
        lec_info = []
        pattern = r"(\d{4})-(\d{1,2})-(\d{1,2})\s+(\d{1,2})[:_](\d{2})[-–](\d{1,2})[:_](\d{2})"
        for lecture in lec_list:
            base = 'https://www.math.pku.edu.cn/kxyj/xsbg/tlb/'
            info_page = base + lecture.find('a')['href']
            title = lecture.find(class_="title").get_text().encode("latin1").decode("utf-8").strip()
            lecturer = lecture.find('p',class_="person").get_text().encode("latin1").decode("utf-8")
            try:
                accurateTime = lecture.find(class_="time").get_text().encode("latin1").decode("utf-8").strip()
                year, month, day, start_time_str1,start_time_str2, end_time_str1, end_time_str2 = re.search(pattern, accurateTime).groups()
                start_time_str = start_time_str1 + ":" + start_time_str2
                end_time_str = end_time_str1 + ":" + end_time_str2
                end = datetime.strptime(f"{year}-{month}-{day} {end_time_str}", "%Y-%m-%d %H:%M")
                date = datetime.strptime(f"{year}-{month}-{day}", "%Y-%m-%d").strftime("%Y-%m-%d")
                this_dict = {"title":title, "start":start_time_str, "end":end_time_str, "lecturer":lecturer, "info_page":info_page, "date" : date}
                if end < today:
                    continue
                lec_info.append(this_dict)
            except:
                #可能需要标记：导入失败，附上网站
                continue
        return lec_info

class eecs(departmentsCrawler):
    def __init__(self):
        super().__init__(dep = "信息科学技术学院")
    def create_events(self):
        self.events.clear()
        events_uncleaned = self.fetch_info() #TODO:如何翻好几页
        #this_dict = {"title":title, "start":start, "info_page":href}
        for event in events_uncleaned:
            standard_event = CalendarEvent(
                title = event["title"],
                time_str = event["start"],
                category = "讲座与报告-信息科学技术学院",
                note = "详情见" + event["info_page"],
                done = False,
                end_time = None
            )
            self.events.append(standard_event)

    def fetch_info(self):
        today = datetime.combine(datetime.today().date(), time())
        url = "https://eecs.pku.edu.cn/index/jzxx.htm"
        res = requests.get(url,headers=self.headers, verify=False)
        web = BeautifulSoup(res.text,'lxml')
        lec_info = []
        list = web.find('ul',class_="list-text")
        lec_list = list.find_all('li')
        pattern = r"(\d{4})年(\d{1,2})月(\d{1,2})日.*?(\d{1,2}:\d{2})"
        for lecture in lec_list:
            href = "https://eecs.pku.edu.cn" + lecture.find('a')['href'][2:]
            title = lecture.find('div',class_="tit").find('div').get_text().encode("latin1").decode("utf-8")
            accurateTime = lecture.find('div',class_="date2").find('p').get_text().encode("latin1").decode("utf-8")
            year, month, day, start_time_str = re.search(pattern, accurateTime).groups()
            start = datetime.strptime(f"{year}-{month}-{day} {start_time_str}", "%Y-%m-%d %H:%M")
            this_dict = {"title":title, "start":start, "info_page":href}
            if start < today:
                continue
            lec_info.append(this_dict)
        return lec_info

m = eecs()
print(m.create_events())
