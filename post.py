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

if data != []:
    for v in data:
        if v['day_of_week'] == dayName:
            attachments = [
                {
                    "fallback": 'アニメの放送時間のご案内',
                    "pretext": '本日放送のアニメ',
                    "fields": [
                        {
                            "title": 'タイトル',
                            "value": v['title'],
                        },
                        {
                            "title": '放送時間',
                            "value": v['publish_at'],
                            "short": "true"
                        },
                        {
                            "title": 'チャンネル',
                            "value": v['channel'],
                            "short": "true"
                        }
                    ]
                }
            ]
            slack.notify(attachments=attachments)
else:
    slack.notify(text="放送予定のアニメがありません")
