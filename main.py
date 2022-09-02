from pprint import pprint
import requests

heroes = [332, 655, 659]
stats = []

def inteligens_request():                                                                     #достаём данные с сайта
    for id in heroes:
       url = f'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/powerstats/{id}.json'
       response = requests.get(url)
       stats.append(response.text)
    pprint(stats)


if __name__ == '__main__':
    inteligens_request()

