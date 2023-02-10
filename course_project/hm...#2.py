import time
import requests
from tqdm import tqdm
from progress_bar import InitBar
"""a = 0
for i in tqdm(range(100)):
    a += 2
    time.sleep(0.1)
print(a)"""
my_token = 'y0_AgAAAAAWHDuNAADLWwAAAADbUSy5AsuaGXp1QMakBiv8qdr4pCKbV4M'
path_on_yadisk = f'/homework/{25}'
url = 'https://sun9-76.userapi.com/impf/c851220/v851220366/af322/QboBF60bOq0.jpg?' \
      'size=1860x1360&quality=96&sign=7160e4fa1efdcf5a75ff4dae46f480d0&' \
      'c_uniq_tag=2swa4XHOdQEgDF9kbQpCc9qzVV6dbcF2ivOqCRGgmv4&type=album'
url_for_upload = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
headers = {'Authorization': 'OAuth %s' % my_token, 'Content-Type': 'application/json'}
params_two = {'path': path_on_yadisk, 'url': url}
response = requests.post(url=url_for_upload, params=params_two, headers=headers)
print(response)
