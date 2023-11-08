import json
import sqlite3
from datetime import datetime
from functionality.common import data_json_for_writing
from functionality.database import Database


class Cipher:
    def __init__(self):
        pass

    def encrypt(self, txt: str) -> str:
        step = 3
        encrypted = ""
        for character in txt:
            if character.isupper():
                character_idx = ord(character) - ord('A')
                character_shift = (character_idx + step) % 26 + ord('A')
                encrypted += chr(character_shift)
            elif character.islower():
                character_idx = ord(character) - ord('a')
                character_shift = (character_idx + step) % 26 + ord('a')
                encrypted += chr(character_shift)
            elif character.isdigit():
                character_new = (int(character) + step) % 10
                encrypted += str(character_new)
            else:
                encrypted += character
        return encrypted

    def decrypt(self, txt: str) -> str:
        step = 3
        decrypted = ""
        step = step % 26
        for character in txt:
            if character.isupper():
                character_idx = ord(character) - ord('A')
                character_org_pos = (character_idx - step) % 26 + ord('A')
                decrypted += chr(character_org_pos)
            elif character.islower():
                character_idx = ord(character) - ord('a')
                character_org_pos = (character_idx - step) % 26 + ord('a')
                decrypted += chr(character_org_pos)
            elif character.isdigit():
                character_org_pos = (int(character) - step) % 10
                decrypted += str(character_org_pos)
            else:
                decrypted += character
        return decrypted

    @staticmethod
    def read_json_data(json_file):
        with open(json_file, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
        return json_data

    @staticmethod
    def write_json_data():
        with Database('json_db.sqlite3') as db:
            cursor = sqlite3.connect('json_db.sqlite3').cursor()
            cursor.execute('SELECT * FROM Ciphers')
            data = cursor.fetchall()

        result = []
        for idx, row in enumerate(data, start=1):
            result.append({
                idx: row
            })
        json_data = json.dumps(result, ensure_ascii=False)

        with open(data_json_for_writing, 'w', encoding='utf-8') as file:
            file.write(json_data)

    def encrypt_json(self, json_file) -> dict:
        encrypted_dict = {}
        data = self.read_json_data(json_file)
        step = 3
        for idx, txt in enumerate(data.values(), start=1):
            encrypted = ''
            for character in txt:
                if character.isupper():
                    character_idx = ord(character) - ord('A')
                    character_shift = (character_idx + step) % 26 + ord('A')
                    encrypted += chr(character_shift)
                elif character.islower():
                    character_idx = ord(character) - ord('a')
                    character_shift = (character_idx + step) % 26 + ord('a')
                    encrypted += chr(character_shift)
                elif character.isdigit():
                    character_new = (int(character) + step) % 10
                    encrypted += str(character_new)
                else:
                    encrypted += character
            encrypted_dict[idx] = encrypted
        with Database('json_db.sqlite3') as db:
            db.add_to_ciphers(datetime.now(), str(encrypted_dict))
        return encrypted_dict

    def decrypt_json(self, json_file) -> dict:
        decrypted_dict = {}
        data = self.read_json_data(json_file)
        step = 3
        for idx, txt in enumerate(data.values(), start=1):
            decrypted = ""
            for character in txt:
                if character.isupper():
                    character_idx = ord(character) - ord('A')
                    character_org_pos = (character_idx - step) % 26 + ord('A')
                    decrypted += chr(character_org_pos)
                elif character.islower():
                    character_idx = ord(character) - ord('a')
                    character_org_pos = (character_idx - step) % 26 + ord('a')
                    decrypted += chr(character_org_pos)
                elif character.isdigit():
                    character_org_pos = (int(character) - step) % 10
                    decrypted += str(character_org_pos)
                else:
                    decrypted += character
            decrypted_dict[idx] = decrypted
        with Database('json_db.sqlite3') as db:
            db.add_to_ciphers(datetime.now(), str(decrypted_dict))
        return decrypted_dict
