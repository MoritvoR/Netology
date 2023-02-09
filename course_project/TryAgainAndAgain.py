import requests
from tqdm import tqdm


def create_folder(my_ya_token: str):
    my_ya_token = 'y0_AgAAAAAWHDuNAADLWwAAAADbUSy5AsuaGXp1QMakBiv8qdr4pCKbV4M'
    url_for_upload = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Authorization': 'OAuth %s' % my_ya_token, 'Content-Type': 'application/json'}
    params = {'path': '/vk_photo'}
    response = requests.put(url=url_for_upload, headers=headers, params=params)
    if response.status_code == 201:
        print('Папка "vk_photo" на Я.Диске создана успешно')
    else:
        print(response.json().get('message'))


if __name__ == '__main__':
    vk_token = input('Введите access_token для VK : ')
    ya_token = input('Введите token для Я.Диска : ')
    id_vk = input('Введите id пользователя из VK : ')


