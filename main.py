import requests


def smartest_hero(heroes):
    list_names = list(heroes.split(', '))
    hero_resp = requests.get("https://akabab.github.io/superhero-api/api/all.json")
    dict_heroes = {hero["name"]: hero["powerstats"]["intelligence"] for hero in hero_resp.json()
                   if hero["name"] in list_names}
    return f'Самый умный герой: {max(dict_heroes, key=dict_heroes.get)} (интеллект = {max(dict_heroes.values())} ед.)'


text = 'Hulk, Captain America, Thanos'
print(smartest_hero(text))
