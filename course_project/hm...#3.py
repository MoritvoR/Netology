'''import requests
my_token = 'y0_AgAAAAAWHDuNAADLWwAAAADbUSy5AsuaGXp1QMakBiv8qdr4pCKbV4M'
url_for_upload = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Authorization': 'OAuth %s' % my_token, 'Content-Type': 'application/json'}
params = {'path': '/vk_photo'}
response = requests.put(url=url_for_upload, headers=headers, params=params)
print(response.json().get('message'))'''
import time
from tqdm import tqdm
#print(time.gmtime(1549543751))
i = 0
tqdm(while i < 20):
    time.sleep(0.2)
    i += 1
