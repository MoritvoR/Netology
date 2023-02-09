import requests
from pprint import pprint
from tqdm import tqdm
import json
if __name__ == '__main__':
    f = open('text.json', 'w')
    my_id = '13761314'
    url = 'https://api.vk.com/method/'
    method = 'photos.get'
    access_token = 'vk1.a.M_oBcOXT2-laBeRZYmohVD2FomiKJ2d_0i_W5xF3qlB1unGBDFIn8nFwY90KXU8J6zxv-tA0AO5SMpDUvuggnbc3tCf7T2ySM-mfWcy330TRYKLftcjfZz0qvkiOdIoHxd7zW-TnjVG0m1LdJ3Q3mtcTrynMejn2fM56AD1ngoq-tGhBA6QFWqHlEkB9lnqIZ3lzgwfMNg4pk0K-yS60FA'
    params = {
        'owner_id': f'{my_id}',
        'album_id': 'profile',
        'rev': 1,
        'extended': 1,
        'count': 5,
        'v': '5.131'
    }
    headers = {'Authorization': f'Bearer {access_token}', 'Content-Type': 'multipart/form-data'}
    response = requests.get(url=url+method, params=params, headers=headers)
    json.dump(response.json(), f, indent=4, )
