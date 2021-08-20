# -*- coding: utf-8 -*-
import os
import json
import urllib.parse
import urllib.request
import datetime
# 環境変数
line_notify_api = os.environ.get('line_notify_api')
line_notify_token = os.environ.get('line_notify_token')
dt_now = datetime.datetime.now()
dt= dt_now.strftime('%Y年%m月%d日')
def lambda_handler(event, context):

    message = "\n\n"+dt + "\n\n修造チャレンジDone！\n明日も頑張れよ！"
    return notify_to_line(message)
def notify_to_line(message):
    
    method = "POST"
    headers = {"Authorization": "Bearer " + line_notify_token}
    payload = {"message": message}
    try:
        payload = urllib.parse.urlencode(payload).encode("utf-8")
        req = urllib.request.Request(line_notify_api, data=payload, method=method, headers=headers)
        urllib.request.urlopen(req)
        return message
    except Exception as e:
        return e