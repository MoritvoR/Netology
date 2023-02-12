import requests
import json
from tqdm import tqdm
import time


class YandexMovements:
    def __init__(self, token):
        self.token = token
        self.headers = {'Authorization': f'OAuth {token}', 'Content-Type': 'application/json'}
        self.url_for_upload = 'https://cloud-api.yandex.net/v1/disk/resources'

    def create_folder(self, name_folder: str):
        """Create new folder on Yandex Disk.
        Return None"""
        params = {'path': f'/{name_folder}'}
        response = requests.put(url=self.url_for_upload, headers=self.headers, params=params)
        if response.status_code == 201:
            print(f'Папка {name_folder} на Я.Диске создана успешно')
            return None
        else:
            print(response.json().get('message'))
            return None

    def upload_to_disk(self, file_urls: list, file_names, name_folder: str):
        '''Upload file on Yandex Disk
        Return None'''
        for file in tqdm(range(len(file_urls))):
            url = file_urls[file]
            name = file_names[file]['file_name']
            path_on_yadisk = f'/{name_folder}/{name}'
            params = {'path': path_on_yadisk, 'url': url}
            response = requests.post(url=self.url_for_upload, params=params, headers=self.headers)
            if response.status_code != 202:
                print(f'При загрузке файла {name} произошла ошибка {response.status_code}: '
                      f'{response.json().get("message")}')
                return None
            return None


class Vk:
    def __init__(self, token, id_target_vk):
        self.get_photo_url = 'https://api.vk.com/method/photos.get'
        self.id_vk = id_target_vk
        self.token = token
        self.headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'multipart/form-data'}

    def _create_name_photo(self, photo_list):
        """Create list photo's name and size"""
        '''for i in tqdm(range(1, len(photo_list))):
            if photo_name == photo_list[i]['file_name']:
                photo_list[i]['file_name'] = f'{photo_list[i]["date"]}.{photo_list[i]["file_name"]}'
                photo_name = photo_list[i]['file_name']
            else:
                photo_list[i]['file_name'] = f'{photo_list[i]["file_name"]}'
        return photo_list'''
        i = 0
        while i < len(photo_list):
            photo_name = photo_list[i]['file_name']
            for k in range(i+1, len(photo_list)):
                if photo_name == photo_list[k]['file_name']:
                    photo_list[k]['file_name'] = f'{photo_list[k]["date"]}.{photo_list[k]["file_name"]}'
                    photo_list[i]['file_name'] = f'{photo_list[i]["date"]}.{photo_list[i]["file_name"]}'
            i += 1
        return photo_list

    def _create_json_file(self, response):
        '''Create json-file "photo_vk_info.json" with information
        about photos'''
        photo_info = []
        all_photo_url = []
        for items in tqdm(response['response']['items']):
            max_size = 0
            file_url = ''
            my_dict = {}
            for sizes in items['sizes']:
                if sizes['height'] * sizes['width'] >= max_size:
                    max_size = sizes['height'] * sizes['width']
                    file_url = sizes['url']
                    file_size = sizes['type']
                    file_date = time.gmtime(items['date'])
                    file_name = f"{items['likes']['count']}.jpg"
                    my_dict = {
                        'file_name': file_name, 'size': file_size,
                        'date': f'{file_date.tm_mday}.{file_date.tm_mon}.{file_date.tm_year}'
                    }
            photo_info.append(my_dict)
            all_photo_url.append(file_url)
        photo_info = self._create_name_photo(photo_info)
        with open('photo_vk_info.json', 'w', encoding='utf-8') as file:
            json.dump(photo_info, file, indent=4)
        return all_photo_url, photo_info

    def get_info_vk(self, photo_counter: int):
        """Get information about photo in profile VK.
        Create json-file 'photo_vk_info.json'.
        Return list photos url and list photo information.
        Version API VK 5.131"""
        params = {
            'owner_id': f'{self.id_vk}',
            'album_id': 'profile',
            'rev': 1,
            'extended': 1,
            'count': photo_counter,
            'v': '5.131'
        }
        response = requests.get(url=self.get_photo_url, params=params, headers=self.headers)
        if response.status_code == 200:
            photo_url_list, photo_information = self._create_json_file(response.json())
            return photo_url_list, photo_information
        else:
            print('При получении информации о фото из VK произошла ошибка.\nПроверьте правильность введённых данных.')
            return None, None


if __name__ == '__main__':
    #vk_token = input('Введите access_token для VK : ')
    vk_token = 'vk1.a.M_oBcOXT2-laBeRZYmohVD2FomiKJ2d_0i_W5xF3qlB1unGBDFIn8nFwY90KXU8J6zxv-tA0AO5SMpDUvuggnbc3tCf7T2ySM-mfWcy330TRYKLftcjfZz0qvkiOdIoHxd7zW-TnjVG0m1LdJ3Q3mtcTrynMejn2fM56AD1ngoq-tGhBA6QFWqHlEkB9lnqIZ3lzgwfMNg4pk0K-yS60FA'
    #ya_token = input('Введите token для Я.Диска : ')
    ya_token = 'y0_AgAAAAAWHDuNAADLWwAAAADbUSy5AsuaGXp1QMakBiv8qdr4pCKbV4M'
    #id_vk = input('Введите id пользователя из VK : ')
    id_vk = '13761314'
    #name_new_folder = input('Введите имя новой папки на Я.Диске для фото из VK : ')
    name_new_folder = 'vk'
    #count_photo = int(input('Введите сколько последних фотографий необходимо загрузить : '))
    count_photo = 5
    '''photo_url, photo_inf = get_info_vk(vk_token, id_vk, count_photo)
    create_folder(ya_token, name_new_folder)
    upload_to_yadisk(ya_token, photo_url, photo_inf, name_new_folder)'''
    get_photo_vk = Vk(vk_token, id_vk)
    upload_photo_disk = YandexMovements(ya_token)
    photos_url, photos_inf = get_photo_vk.get_info_vk(count_photo)
    upload_photo_disk.create_folder(name_new_folder)
    upload_photo_disk.upload_to_disk(photos_url, photos_inf, name_new_folder)