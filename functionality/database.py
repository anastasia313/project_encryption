import sqlite3


class Database:
    def __init__(self, path):
        self.con = sqlite3.connect(path)

    def create_table(self):
        query = 'CREATE TABLE IF NOT EXISTS Ciphers(id INTEGER PRIMARY KEY, date DATE NOT NULL, cipher TEXT NOT NULL);'
        self.con.execute(query)

    def add_to_ciphers(self, date, cipher):
        self.create_table()
        query = "INSERT INTO Ciphers(date, cipher) VALUES(?, ?)"
        self.con.execute(query, (date, cipher))

    def preview_table(self, table_name):
        query = f'SELECT * FROM {table_name}'
        result = self.con.execute(query).fetchall()
        print(result)

    def delete_data(self, table_name, value):
        query = f'DELETE FROM {table_name} WHERE id = ?'
        self.con.execute(query, (value,))

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        if isinstance(exc_value, Exception):
            self.con.rollback()
        else:
            self.con.commit()

        self.con.close()
