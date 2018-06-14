import pprint
import json
import requests
import settings
import numpy as np
import string
import random
from time import sleep
n = 5
base_latitude = 35.5557638
base_longitude = 139.362238


# %%
for i in range(100):
    random_str = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(n)])
    rand_lat = 35.5557638 + 0.001*np.random.randn()
    rand_long = 139.362238 + 0.001*np.random.randn()
    rand_nickname = random.choice(['太郎', 'たかし', 'アンドリュー', '慶一', '大輔', '大河', '淳一'])

    u_data = {
        'username':random_str,
        'email': random_str+'@mail.com',
        'point': 0,
        'latitude': rand_lat,
        'longitude': rand_long,
        'nickname': nickname
    }

    response = requests.post(
        'http://0.0.0.0:80/user',
        json.dumps(u_data),
        headers={'Content-Type': 'application/json'}
    )
    sleep(0.5)

    # pprint.pprint(response.json())


# %%
LINE_API_KEY = settings.LINE_API_KEY
wu_data = {
    'username':'keix1',
    'major': 38649,
    'minor': 30703,
    'latitude': '35.6694219',
    'longitude': '139.4612045',
    'line_token': 'n72C4LeMXBDsl3Y4oR7GCspgoY7sloDG23ygRRFYRhg'
}

response = requests.post(
    'http://0.0.0.0:80/watched_user',
    json.dumps(wu_data),
    headers={'Content-Type': 'application/json'}
)
pprint.pprint(response.json())


# %%
ap_data = {
    'username':'keix1',
    'major': 38649,
    'minor': 30703,
    'latitude': '35.6694219',
    'longitude': '139.4612045'
}

response = requests.post(
    # 'http://0.0.0.0:80/user/me',
    'https://mimaco.herokuapp.com/user/keix1',
    json.dumps(ap_data),
    headers={'Content-Type': 'application/json'}
)
pprint.pprint(response.json())
