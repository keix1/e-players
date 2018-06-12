import pprint
import json
import requests

def main():
    # u_data = {
    #     'username':'me',
    #     'email': 'me@mail.com',
    #     'point': 0
    # }
    #
    # response = requests.post(
    #     'http://0.0.0.0:80/user',
    #     json.dumps(u_data),
    #     headers={'Content-Type': 'application/json'}
    # )
    # pprint.pprint(response.json())


    # wu_data = {
    #     'username':'you',
    #     'major': 11111,
    #     'minor': 22222,
    #     'latitude': '123',
    #     'longitude': '456'
    # }
    #
    # response = requests.post(
    #     'http://0.0.0.0:80/watched_user',
    #     json.dumps(wu_data),
    #     headers={'Content-Type': 'application/json'}
    # )
    # pprint.pprint(response.json())

    ap_data = {
        'username':'me',
        'major': 11111,
        'minor': 22222,
        'latitude': '12345',
        'longitude': '45678'
    }

    response = requests.post(
        'http://0.0.0.0:80/user/me',
        # 'https://mimaco.herokuapp.com/user/me',
        json.dumps(ap_data),
        headers={'Content-Type': 'application/json'}
    )
    pprint.pprint(response.json())

if __name__=='__main__':
    main()
