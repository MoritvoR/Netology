import requests

ya_token = 'y0_AgAAAAAWHDuNAADLWwAAAADbUSy5AsuaGXp1QMakBiv8qdr4pCKbV4M'
url = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Authorization': f'OAuth {ya_token}',
               'Content-Type': 'application/json'}
params = {'path': f'/'}
response = requests.get(url=url, headers=headers, params=params)
print(response)
my_json = response.json()
name = ''
for i in my_json['_embedded']['items']:
    if i['name'] == 'new_folder':
        name = i['name']
        break

