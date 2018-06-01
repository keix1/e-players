import pprint
import json
import requests

def main():
    # data = {
    #     'username':'me',
    #     'email': 'me@mail.com',
    #     'point': 0
    # }
    #
    # response = requests.post(
    #     'http://127.0.0.1:5000/user',
    #     json.dumps(data),
    #     headers={'Content-Type': 'application/json'}
    # )
    # pprint.pprint(response.json())


    data = {
        'username':'you',
        'major': 11111,
        'minor': 22222
    }

    response = requests.post(
        'http://127.0.0.1:5000/watched_user',
        json.dumps(data),
        headers={'Content-Type': 'application/json'}
    )
    pprint.pprint(response.json())

if __name__=='__main__':
    main()
