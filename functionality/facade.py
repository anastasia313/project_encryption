import logging
import json
from common import data_json_for_writing

class Facade:
    def __init__(self, cipher):
        self.cipher = cipher

    def menu(self):
        while True:
            print("Please choose an option:")
            print("1. Encrypt text")
            print("2. Decrypt text")
            print("3. Encrypt JSON file")
            print("4. Decrypt JSON file")
            print("5. Show the history")
            print("6. Exit")
            choice = input()

            if choice == '1':
                txt = input('Please enter data for encryption')
                self.cipher.encrypt(txt)
                logging.info("User has encrypted data")
                print(f'Your result - {self.cipher.encrypt(txt)}')
            elif choice == '2':
                txt = input('Please enter data for decryption')
                self.cipher.decrypt(txt)
                logging.info("User has decrypted data")
                print(f'Your result - {self.cipher.decrypt(txt)}')
            elif choice == '3':
                file = input('Please provide file for encryption')
                self.cipher.encrypt_json(file)
                logging.info("User has encrypted json data")
                print(f'Your result - {self.cipher.encrypt_json(file)}')
            elif choice == '4':
                file = input('Please provide file for decryption')
                self.cipher.decrypt_json(file)
                logging.info("User has decrypted json data")
                print(f'Your result - {self.cipher.decrypt_json(file)}')
            elif choice == '5':
                self.cipher.write_json_data()
                logging.info("User has requested history")
                with open(data_json_for_writing, 'r') as file:
                    json_data = json.load(file)
                    print(json_data)
            elif choice == '6':
                logging.info("User has exited")
                return f'You exit'
            else:
                print(f"Wrong input!")
