import sqlite3
from datetime import datetime

from src.cipher import Cipher
from src.const import JSON_RESULT_FILE_NAME
import pytest


def test_write_json_data():
    db_path = "../tests/json_db.sqlite3"
    with open(JSON_RESULT_FILE_NAME, 'w+'):
        pass

    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Ciphers(id INTEGER PRIMARY KEY, date DATE NOT NULL, cipher TEXT NOT NULL)')
        cursor.execute('DELETE FROM Ciphers')
        date = "2023-11-20 15:11:22.906568"
        cipher = "{'cipher':'bcde'}"
        cursor.execute("INSERT INTO Ciphers(date, cipher) VALUES(?, ?)", (date, cipher))
        connection.commit()

    Cipher.write_json_data(db_path)

    with open(JSON_RESULT_FILE_NAME, 'r', encoding='utf-8') as file:
        data = file.read()
    assert "[{\"1\": [1, \"2023-11-20 15:11:22.906568\", \"{'cipher':'bcde'}\"]}]" == data

