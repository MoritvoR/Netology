import requests
if __name__ == '__main__':
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url=url)
    heroes = {}
    for now in response.json():
        heroes[now['name']] = now['powerstats']['intelligence']
    needed_heroes = ['Hulk', 'Captain America', 'Thanos']
    clever = [0, 'name']
    for i in needed_heroes:
        if heroes[i] >= clever[0]:
            clever[0] = heroes[i]
            clever[1] = i
    print(f'Самый умный: {clever[1]}. Его интеллект:{clever[0]}')

