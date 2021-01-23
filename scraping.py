import requests
from bs4 import BeautifulSoup
from os import getenv
import json
import utils

u = utils.UtilsClass()

load_url = getenv('SCRAPING_TARGET_URL')
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")


def writtenJson(jsonList, year, month):
    with open(f'./data/tokyo_mx_only/{year}{month}.json', 'w') as f:
        json.dump(jsonList, f, ensure_ascii=False, indent=4)


def makeJsonList(soup):
    jsonList = []
    for e in soup.find(class_='week_area').find_all('li'):
        week = u.convertDayOfWeek(
            e.find(class_="oatime").find(class_='youbi').text)
        e.find(class_="oatime").find(class_='youbi').decompose()
        e.find('h4').find('strong').decompose()
        item = {
            'title': e.find('h4').text,
            'publish_at': e.find(class_="oatime").text,
            'channel': 'TOKYO MX',
            'day_of_week': week
        }
        jsonList.append(item)
    return jsonList


writtenJson(makeJsonList(soup), u.year, u.month)
