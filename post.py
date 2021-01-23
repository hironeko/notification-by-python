import json
import slackweb
from os import getenv
import utils

u = utils.UtilsClass()


def getData(year, month):
    anime = json.load(open(f'./data/new_anime/{year}{month}.json', 'r'))
    tmo = json.load(open(f'./data/tokyo_mx_only/{year}{month}.json', 'r'))
    return anime + tmo


def toSlack(data, dayName):
    slack = slackweb.Slack(url=getenv('SLACK_WEBHOOK_URL'))
    items = []
    if data != []:
        attachments = {
            "fallback": 'アニメの放送時間のご案内',
            "pretext": '本日放送のアニメ',
        }
        for v in data:
            if v['day_of_week'] == dayName:
                items.append({
                    "title": 'タイトル',
                    "value": v['title'],
                })
                items.append({
                    "title": '放送時間',
                    "value": v['publish_at'],
                    "short": "true"
                })
                items.append({
                    "title": 'チャンネル',
                    "value": v['channel'],
                    "short": "true"
                })
        attachments['fields'] = items
        slack.notify(attachments=[attachments])
    else:
        slack.notify(text="放送予定のアニメがありません")


toSlack(
    getData(u.year, u.month),
    u.dayName
)
