import json
import sqlite3
from datetime import datetime
from src.const import JSON_RESULT_FILE_NAME, NUMBER_OF_ALPHABETICAL_LETTERS, NUMBERS_OF_DIGITS, STEP
from src.database import Database


# TODO
#
class EnteredZeroStep(Exception):
    def __str__(self):
        return 'You entered 0. Please enter step more than 0'


class EnteredNegativeStep(Exception):
    def __str__(self):
        return 'You entered negative step. Please enter step more than 0'


class EnteredStepMoreThanAlphabet(Exception):
    def __str__(self):
        return 'You entered value more than alphabet. Please enter correct step'


class ProvidedEmptyData(Exception):
    def __str__(self):
        return 'Your file is empty. Nothing for encryption'


class Cipher:
    def shift_character(self, txt: str, step: int) -> str:
        for character in txt:
            if character.isupper():
                character_idx = ord(character) - ord('A')
                character_shift = (character_idx + step) % NUMBER_OF_ALPHABETICAL_LETTERS + ord('A')
                return chr(character_shift)
            elif character.islower():
                character_idx = ord(character) - ord('a')
                character_shift = (character_idx + step) % NUMBER_OF_ALPHABETICAL_LETTERS + ord('a')
                return chr(character_shift)
            elif character.isdigit():
                character_new = (int(character) + step) % NUMBERS_OF_DIGITS
                return str(character_new)
            else:
                return character

    def encrypt(self, txt: str, step: int, sign_flag: bool) -> str:
        if 27 > step > 0:
            shift = step if sign_flag else -step
            encrypted_sentence = ''
            for character in txt:
                encrypted_sentence += self.shift_character(character, shift)
            with Database('json_db.sqlite3') as db:
                db.add_to_ciphers(datetime.now(), str(encrypted_sentence))
            return encrypted_sentence
        elif step == 0:
            raise EnteredZeroStep
        elif step < 0:
            raise EnteredNegativeStep
        else:
            raise EnteredStepMoreThanAlphabet

    @staticmethod
    def read_json_data(json_file):
        with open(json_file, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
        return json_data

    @staticmethod
    def write_json_data(path):
        with Database(path) as db:
            cursor = db.con.cursor()
            cursor.execute('SELECT * FROM Ciphers')
            data = cursor.fetchall()

        result = []
        for idx, row in enumerate(data, start=1):
            result.append({
                idx: row
            })
        json_data = json.dumps(result, ensure_ascii=False)

        with open(JSON_RESULT_FILE_NAME, 'w', encoding='utf-8') as file:
            file.write(json_data)

    def encrypt_json(self, json_file, sign_flag: bool) -> dict:
        encrypted_dict = {'data': []}
        data = self.read_json_data(json_file)
        if data != {}:
            for entry in data['data']:
                if 27 > entry['shift'] > 0:
                    shift = entry['shift'] if sign_flag else -entry['shift']
                    encrypted = ''
                    for txt in entry['text']:
                        encrypted += self.shift_character(txt, shift)
                    encrypted_dict['data'].append({'cipher': encrypted})
                elif entry['shift'] == 0:
                    raise EnteredZeroStep
                elif entry['shift'] < 0:
                    raise EnteredNegativeStep
                else:
                    raise EnteredStepMoreThanAlphabet
            if encrypted_dict != {}:
                with Database('json_db.sqlite3') as db:
                    db.add_to_ciphers(datetime.now(), str(encrypted_dict))
                return encrypted_dict
            else:
                raise ProvidedEmptyData
        else:
            raise ProvidedEmptyData