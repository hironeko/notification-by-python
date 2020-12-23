import json
import slackweb
from os import getenv

data = json.load(open('./data/anime/202001.json', 'r'))

webhookUrl = getenv('SLACK_WEBHOOK_URL')

slack = slackweb.Slack(
    url=webhookUrl)

for v in data:
    print(v['title'])
    slack.notify(text=v['title'])
