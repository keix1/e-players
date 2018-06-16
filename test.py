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

# LINE_API_KEY = settings.LINE_API_KEY


# add fixed usr
# %%
matsuoka_token_point = "KoZEi70uHqzOJUabiwAFM4rJDV1VLFBDxBR1ABHbcOl"
u_data = {
    'username':'grandpa',
    'email': 'grandpa@mail.com',
    'point': 0,
    'latitude': base_latitude,
    'longitude': base_longitude,
    'nickname': 'おじいちゃん',
    'line_token': matsuoka_token_point
}

response = requests.post(
    'http://0.0.0.0:80/user',
    # 'https://mimaco.herokuapp.com/user',
    json.dumps(u_data),
    headers={'Content-Type': 'application/json'}
)

# add random usr
# %%
for i in tqdm(range(1000)):
    random_str = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(n)])
    rand_lat = base_latitude + 0.1*np.random.randn()
    rand_long = base_longitude + 0.1*np.random.randn()
    rand_nickname = random.choice(['太郎', 'たかし', 'アンドリュー', '慶一', '大輔', '大河', '淳一', '優子', 'りか', 'まき', 'りさ', 'みゆき', 'えり', '香織', 'りさ', 'はるか', 'あやか'])
    random_token = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(10)])

    u_data = {
        'username':random_str,
        'email': random_str+'@mail.com',
        'point': 0,
        'latitude': rand_lat,
        'longitude': rand_long,
        'nickname': rand_nickname,
        'line_token': random_token
    }

    response = requests.post(
        'http://0.0.0.0:80/user',
        json.dumps(u_data),
        headers={'Content-Type': 'application/json'}
    )
    # sleep(0.01)

    # pprint.pprint(response.json())


# add fixed watched_usr
# %%
# LINE_API_KEY = "n72C4LeMXBDsl3Y4oR7GCspgoY7sloDG23ygRRFYRhg"
inoue_token_location = "f2Eoo0VMHEs9itKXkZPfdc00vw8DSDX4ZkjmKZyzW1c"
horikawa_token_location = "gyxrhlQUpZdZpAWxMqvfooYrTxZ3fbI0el3TCZ8ecj0"

major_list = [18550,38649,40566,45648,52607]
minor_list = [57937,30703,31949,8669,9706]
for i in tqdm(range(len(major_list))):
    wu_data = {
        'username':'keix'+str(i+1),
        'major': major_list[i],
        'minor': minor_list[i],
        'latitude': '35.6694219',
        'longitude': '139.4612045',
        'line_token': horikawa_token_location,
        'nickname': '子ども',
        'pointrate': 1
    }

    response = requests.post(
        'http://0.0.0.0:80/watched_user',
        json.dumps(wu_data),
        headers={'Content-Type': 'application/json'}
    )
    # pprint.pprint(response.json())

# add random watched_usr
# %%
for i in tqdm(range(100)):
    random_str = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(n)])
    rand_lat = base_latitude + 0.1*np.random.randn()
    rand_long = base_longitude + 0.1*np.random.randn()
    rand_nickname = random.choice(['太郎', 'たかし', 'アンドリュー', '慶一', '大輔', '大河', '淳一', '優子', 'りか', 'まき', 'りさ', 'みゆき', 'えり', '香織', 'りさ', 'はるか', 'あやか'])
    rand_rate = random.choice([1,2,3])
    rand_major = random.randint(10000, 99999)
    rand_minor = random.randint(10000, 99999)
    u_data = {
        'username':random_str,
        'major': rand_major,
        'minor': rand_minor,
        'latitude': rand_lat,
        'longitude': rand_long,
        'line_token': horikawa_token_location,
        'nickname': rand_nickname,
        'pointrate': rand_rate
    }

    response = requests.post(
        'http://0.0.0.0:80/watched_user',
        json.dumps(u_data),
        headers={'Content-Type': 'application/json'}
    )
    sleep(0.01)

    # pprint.pprint(response.json())



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
