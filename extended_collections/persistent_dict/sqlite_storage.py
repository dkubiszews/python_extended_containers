# TODO: add copyrights

import sqlite3


class SQLiteStorage:
    def __init__(self, storage_path):
        self.sqlite_connection = sqlite3.connect(storage_path)

    def open(self):
        cursor = self.sqlite_connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS key_value_pairs (key text, value text)')
        self.sqlite_connection.commit()

    def write(self, key, value):
        cursor = self.sqlite_connection.cursor()
        cursor.execute('INSERT INTO key_value_pairs VALUES (?, ?)', (key, value))
        self.sqlite_connection.commit()

    def remove(self, key):
        cursor = self.sqlite_connection.cursor()
        cursor.execute('DELETE FROM key_value_pairs WHERE key=?', (key,))
        self.sqlite_connection.commit()

        # TODO: write tests
        return cursor.rowcount != 0

    def read(self, key):
        cursor = self.sqlite_connection.cursor()
        cursor.execute('SELECT value FROM key_value_pairs WHERE key=?', (key,))
        result = cursor.fetchone()
        if result is None:
            return None
        return result[0]

    def read_key_generator(self):
        cursor = self.sqlite_connection.cursor()
        cursor.execute('SELECT key FROM key_value_pairs')
        for key in cursor:
            yield key[0]

    def read_value_generator(self):
        cursor = self.sqlite_connection.cursor()
        cursor.execute('SELECT value FROM key_value_pairs')
        for value in cursor:
            yield value[0]

    def read_key_value_generator(self):
        cursor = self.sqlite_connection.cursor()
        cursor.execute('SELECT key, value FROM key_value_pairs')
        for key_value_pair in cursor:
            yield key_value_pair[0], key_value_pair[1]
