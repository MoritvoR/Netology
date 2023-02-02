import requests

token = 'y0_AgAAAAAWHDuNAADLWwAAAADbUSy5AsuaGXp1QMakBiv8qdr4pCKbV4M'
common_url = 'https://cloud-api.yandex.net/v1/'
path_on_yadisk = '/homework/Ошибка_параллели.docx'
path_on_computer = 'D:/Книга_1/Ошибка_параллели.docx'
headers = {'Authorization': 'OAuth %s' % token, 'Content-Type': 'application/json'}
url_for_upload = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
params = {'path': path_on_yadisk, 'owerwrite': 'true'}
get_upload_url = requests.get(url=url_for_upload, headers=headers, params=params)
href = get_upload_url.json().get('href')
print(href)
response = requests.put(url=href, data=open(path_on_computer, 'rb'))
if response.status_code == 201:
    print("Mission complete! :-) ")
