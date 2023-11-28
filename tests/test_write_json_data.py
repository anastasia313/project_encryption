import sqlite3
from datetime import datetime

from project_encryption.src.cipher import Cipher
from project_encryption.src.const import JSON_RESULT_FILE_NAME
import pytest


def test_write_json_data(prepare_db):
    db_path = "../tests/json_db.sqlite3"
    with open(JSON_RESULT_FILE_NAME, 'w'):
        pass

    with sqlite3.connect(db_path) as connection:
        prepare_db(connection)

    Cipher.write_json_data(db_path)

    with open(JSON_RESULT_FILE_NAME, 'r', encoding='utf-8') as file:
        data = file.read()
    assert "[{\"1\": [1, \"2023-11-20 15:11:22.906568\", \"{'cipher':'bcde'}\"]}]" == data
