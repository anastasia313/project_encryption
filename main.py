import logging
from src.database import Database
from src.facade import Facade
from src.cipher import Cipher


def main():
    logging.basicConfig(filename='app.log', level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")

    with Database('json_db.sqlite3') as db:
        db.create_table()
        db.preview_table('Ciphers')

    cipher = Cipher()
    Facade(cipher)


if __name__ == '__main__':
    main()
