#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import settings

# LINE_API_KEY = settings.LINE_API_KEY
#
# def lineNotify(message):
#     line_notify_token = LINE_API_KEY
#     line_notify_api = 'https://notify-api.line.me/api/notify'
#     payload = {'message': message}
#     headers = {'Authorization': 'Bearer ' + line_notify_token}
#     requests.post(line_notify_api, data=payload, headers=headers)

def lineNotify(message,line_notify_token):
    line_notify_api = 'https://notify-api.line.me/api/notify'
    # payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    requests.post(line_notify_api, data=message, headers=headers)

if __name__ == '__main__':
    lineNotify('ニャア')
