import logging
from database import Database
from facade import Facade
from cipher_implementation import Cipher

logging.basicConfig(filename='app.log', level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")

with Database('json_db.sqlite3') as db:
    db.create_table()
    db.preview_table('Ciphers')

cipher = Cipher()
facade = Facade(cipher)
facade.menu()
