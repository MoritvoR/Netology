import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.headers = {'Authorization': 'OAuth %s' % token, 'Content-Type': 'application/json'}

    def upload(self, path_yadisk: str, path_computer: str):
        """Метод загружает файлы на яндекс диск"""
        url_for_upload = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': path_yadisk, 'overwrite': 'true'}
        get_upload_url = requests.get(url=url_for_upload, headers=self.headers, params=params)
        href = get_upload_url.json().get('href')
        with open(path_computer, 'rb') as file:
            response = requests.put(url=href, data=file)
            if response.status_code == 201:
                print("Mission complete! :-) ")
                return None
            else:
                print('Alarm! Alarm! Какая-то ошибка! :-|')
                return None


if __name__ == '__main__':
    my_token = 'y0_AgAAAAAWHDuNAADLWwAAAADbUSy5AsuaGXp1QMakBiv8qdr4pCKbV4M'
    path_on_yadisk = '/homework/Ошибка_параллели.docx'
    path_on_computer = 'D:/Книга_1/Ошибка_параллели.docx'
    uploader = YaUploader(my_token)
    uploader.upload(path_yadisk=path_on_yadisk, path_computer=path_on_computer)
