from course_project.TryAgainAndAgain import YandexMovements
import requests


def test_create_folder(name_folder='test_folder'):
    ya_token = ''
    creator_new_folder = YandexMovements(ya_token)
    result = creator_new_folder.create_folder(name_folder)
    assert result.status_code == 201, f'Код ошибки:{result.status_code}. ' \
                                      f'{result.json().get("message")}'

    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Authorization': f'OAuth {ya_token}',
               'Content-Type': 'application/json'}
    params = {'path': f'/'}
    response = requests.get(url=url, headers=headers, params=params)
    my_json = response.json()
    name = ''
    for i in my_json['_embedded']['items']:
        if i['name'] == name_folder:
            name = i['name']
            break
    assert name == name_folder, 'Папка не создана!'
