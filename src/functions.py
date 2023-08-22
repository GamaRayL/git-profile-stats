import requests


# get_repos_stats(), которая собирает статистику по репозиториям заданного пользователя на GitHub.
# Эта функция использует библиотеку requests, чтобы обращаться к API GitHub
# и получать информации о репозиториях пользователя.
# Затем функция обрабатывает полученные данные и возвращает список словарей,
# содержащих статистику по каждому репозиторию.

def get_repos_stats(username):
    url = f'https://api.github.com/users/{username}/repos'

    try:
        response = requests.get(url)
        repos = response.json()
        print(repos)
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error")
        print(errh.args[0])
    except requests.exceptions.ReadTimeout:
        print("Time out")
    except requests.exceptions.ConnectionError:
        print("Connection error")
    except requests.exceptions.RequestException:
        print("Exception request")


get_repos_stats('gamarayl')
