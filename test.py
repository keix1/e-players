import pprint
import json
import requests
import settings
import numpy as np
import string
import random
from time import sleep
n = 5
base_latitude = 35.53535
base_longitude = 139.700954
from tqdm import tqdm

# %%
u_data = {
    'username':'grandpa',
    'email': 'grandpa@mail.com',
    'point': 0,
    'latitude': base_latitude,
    'longitude': base_longitude,
    'nickname': 'おじいちゃん'
}

response = requests.post(
    'http://0.0.0.0:80/user',
    # 'https://mimaco.herokuapp.com/user',
    json.dumps(u_data),
    headers={'Content-Type': 'application/json'}
)

# %%
for i in tqdm(range(10000)):
    random_str = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(n)])
    rand_lat = base_latitude + 0.1*np.random.randn()
    rand_long = base_longitude + 0.1*np.random.randn()
    rand_nickname = random.choice(['太郎', 'たかし', 'アンドリュー', '慶一', '大輔', '大河', '淳一', '優子', 'りか', 'まき', 'りさ', 'みゆき', 'えり', '香織', 'りさ', 'はるか', 'あやか'])

    u_data = {
        'username':random_str,
        'email': random_str+'@mail.com',
        'point': 0,
        'latitude': rand_lat,
        'longitude': rand_long,
        'nickname': rand_nickname
    }

    response = requests.post(
        'http://0.0.0.0:80/user',
        json.dumps(u_data),
        headers={'Content-Type': 'application/json'}
    )
    # sleep(0.01)

    # pprint.pprint(response.json())


# %%
LINE_API_KEY = settings.LINE_API_KEY

wu_data = {
    'username':'keix1',
    'major': 38649,
    'minor': 30703,
    'latitude': '35.6694219',
    'longitude': '139.4612045',
    'line_token': LINE_API_KEY,
    'nickname': 'けいいち',
    'pointrate': 1
}

response = requests.post(
    'http://0.0.0.0:80/watched_user',
    json.dumps(wu_data),
    headers={'Content-Type': 'application/json'}
)
pprint.pprint(response.json())


# %%
for i in tqdm(range(10000)):
    random_str = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(n)])
    rand_lat = base_latitude + 0.1*np.random.randn()
    rand_long = base_longitude + 0.1*np.random.randn()
    rand_nickname = random.choice(['太郎', 'たかし', 'アンドリュー', '慶一', '大輔', '大河', '淳一', '優子', 'りか', 'まき', 'りさ', 'みゆき', 'えり', '香織', 'りさ', 'はるか', 'あやか'])
    rand_rate = random,choice([1,2,3])
    u_data = {
        'username':random_str,
        'major': 38649,
        'minor': 30703,
        'latitude': rand_lat,
        'longitude': rand_long,
        'line_token': LINE_API_KEY,
        'nickname': rand_nickname,
        'pointrate': rand_rate
    }

    response = requests.post(
        'http://0.0.0.0:80/user',
        json.dumps(u_data),
        headers={'Content-Type': 'application/json'}
    )
    # sleep(0.01)

    # pprint.pprint(response.json())


KEYS = [LINE_API_KEY1,LINE_API_KEY2]

# %%
ap_data = {
    'username':'bmg0l',
    'major': 38649,
    'minor': 30703,
    'latitude': '35.6694219',
    'longitude': '139.4612045'
}

response = requests.post(
    'http://0.0.0.0:80/user/me',
    # 'https://mimaco.herokuapp.com/user/keix1',
    json.dumps(ap_data),
    headers={'Content-Type': 'application/json'}
)
pprint.pprint(response.json())
