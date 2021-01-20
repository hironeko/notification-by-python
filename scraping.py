import requests
from bs4 import BeautifulSoup
from os import getenv
import json
import datetime as dt
import calendar

today = dt.date.today()
dayName = calendar.day_name[today.weekday()]

if today.month < 10:
    month = f'0{today.month}'
else:
    month = today.month

weekList = {
    '月': 'Monday',
    '火': 'Tuesday',
    '水': 'Wednesday',
    '木': 'Thursday',
    '金': 'Friday',
    '土': 'Saturday',
    '日': 'Sunday'
}

load_url = getenv('SCRAPING_TARGET_URL')
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# アニメの一覧を取得
animeList = soup.find(class_='week_area').find_all('li')

jsonList = []
for e in soup.find(class_='week_area').find_all('li'):
    week = weekList[e.find(class_="oatime").find(class_='youbi').text]
    e.find(class_="oatime").find(class_='youbi').decompose()
    e.find('h4').find('strong').decompose()
    item = {
        'title': e.find('h4').text,
        'publish_at': e.find(class_="oatime").text,
        'channel': 'TOKYO MX',
        'day_of_week': week
    }
    jsonList.append(item)


with open(f'./data/new_anime/{today.year}{month}.json', 'w') as f:
    json.dump(jsonList, f, ensure_ascii=False, indent=4)
