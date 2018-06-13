import pprint
import json
import requests
import settings


# %%
u_data = {
    'username':'me',
    'email': 'me@mail.com',
    'point': 0
}

response = requests.post(
    'http://0.0.0.0:80/user',
    json.dumps(u_data),
    headers={'Content-Type': 'application/json'}
)
pprint.pprint(response.json())


# %%
LINE_API_KEY = settings.LINE_API_KEY
wu_data = {
    'username':'you',
    'major': 11111,
    'minor': 22222,
    'latitude': '123',
    'longitude': '456',
    'line_token': LINE_API_KEY
}

response = requests.post(
    'http://0.0.0.0:80/watched_user',
    json.dumps(wu_data),
    headers={'Content-Type': 'application/json'}
)
pprint.pprint(response.json())


# %%
ap_data = {
    'username':'me',
    'major': 11111,
    'minor': 22222,
    'latitude': '35.6694219',
    'longitude': '139.4612045'
}

response = requests.post(
    'http://0.0.0.0:80/user/me',
    # 'https://mimaco.herokuapp.com/user/me',
    json.dumps(ap_data),
    headers={'Content-Type': 'application/json'}
)
pprint.pprint(response.json())
