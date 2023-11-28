from src.cipher import Cipher, EnteredZeroStep, EnteredNegativeStep, EnteredStepMoreThanAlphabet
import pytest

@pytest.fixture
def prepare_db(connection):
    cursor = connection.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS Ciphers(id INTEGER PRIMARY KEY, date DATE NOT NULL, cipher TEXT NOT NULL)')
    cursor.execute('DELETE FROM Ciphers')
    date = "2023-11-20 15:11:22.906568"
    cipher = "{'cipher':'bcde'}"
    cursor.execute("INSERT INTO Ciphers(date, cipher) VALUES(?, ?)", (date, cipher))
    connection.commit()
