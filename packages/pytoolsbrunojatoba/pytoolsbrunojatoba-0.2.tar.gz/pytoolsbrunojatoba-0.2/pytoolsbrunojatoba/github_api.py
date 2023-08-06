import requests as rq


def buscar_avatar(usuario):
    url = f'https://api.github.com/users/{usuario}'
    answer = rq.get(url)
    return answer.json()['avatar_url']


print(buscar_avatar('brjatoba92'))
