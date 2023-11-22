import logging
import json
from src.const import JSON_RESULT_FILE_NAME


class Facade:
    def __init__(self, cipher):
        self.cipher = cipher
        self.__is_running = True
        self.options = {
            '1': self._encrypt_txt,
            '2': self._decrypt_txt,
            '3': self._encrypt_json,
            '4': self._decrypt_json,
            '5': self._show_history,
            '6': self._close_app,
        }
        self.initialize()

    def initialize(self):
        while self.__is_running:
            self._show_menu()
            self._get_and_execute_choice()

    def _show_menu(self):
        menu = (
            """
            Please choose an option:
            1. Encrypt text
            2. Decrypt text
            3. Encrypt JSON file
            4. Decrypt JSON file
            5. Show the history
            6. Exit
            """
        )
        print(menu)

    def _get_and_execute_choice(self):
        user_choice = input('Choose what you want to do: ')
        try:
            self.options.get(user_choice, self._show_error)()
        except Exception as e:
            logging.exception(e)
            print(f'\n EXCEPTION \n {e}')

    def _encrypt_txt(self):
        txt = input('Please enter data for encryption')
        step = int(input('Please enter step for encryption'))
        result = self.cipher.encrypt(txt, step, True)
        logging.info("User has encrypted data")
        print(f'Your result - {result}')

    def _decrypt_txt(self):
        txt = input('Please enter data for decryption')
        step = int(input('Please enter step for decryption'))
        result = self.cipher.encrypt(txt, step, False)
        logging.info("User has decrypted data")
        print(f'Your result - {result}')

    def _encrypt_json(self):
        file = input('Please provide file for encryption')
        result = self.cipher.encrypt_json(file, True)
        logging.info("User has encrypted json data")
        print(f'Your result - {result}')

    def _decrypt_json(self):
        file = input('Please provide file for decryption')
        result = self.cipher.encrypt_json(file, False)
        logging.info("User has decrypted json data")
        print(f'Your result - {result}')

    def _show_history(self):
        self.cipher.write_json_data("json_db.sqlite3")
        logging.info("User has requested history")
        with open(JSON_RESULT_FILE_NAME, 'r') as file:
            json_data = json.load(file)
            print(json_data)

    def _close_app(self):
        self.__is_running = False
        logging.info("User has exited")

    def _show_error(self):
        print(f"Wrong input!")
