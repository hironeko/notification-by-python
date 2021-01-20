import json
import slackweb
from os import getenv
import datetime as dt
import calendar

today = dt.date.today()
dayName = calendar.day_name[today.weekday()]

if today.month < 10:
    month = f'0{today.month}'
else:
    month = today.month

data = json.load(open(f'./data/anime/{today.year}{month}.json', 'r'))

slack = slackweb.Slack(url=getenv('SLACK_WEBHOOK_URL'))

attachments = {
    "fallback": 'アニメの放送時間のご案内',
    "pretext": '本日放送のアニメ',
}
items = []
if data != []:
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
