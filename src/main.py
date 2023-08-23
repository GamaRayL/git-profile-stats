from src.config import config
from src.functions import get_repos_stats
from src.postgres_db import PostgresDB


def main():
    params = config()

    stats = get_repos_stats('gamarayl')
    db = PostgresDB('git_user_repo', params)
    db.insert_data(stats)

    for item in db.get_data(10, 'name'):
        print(item)

    db.export_to_json()


if __name__ == '__main__':
    main()
