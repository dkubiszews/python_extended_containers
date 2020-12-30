# TODO: add copyrights

from hashlib import sha256

from extended_collections.persistent_dict.sqlite_storage import SQLiteStorage


class PersistentDict:
    """
    Dict stored on disk.
    """

    def __init__(self, storage_path, initial_value=None):
        self.__storage = SQLiteStorage(storage_path)
        self.__storage.open()

        if initial_value is not None:
            if not isinstance(initial_value, dict):
                raise TypeError("The 'initial_value' must be dict type")
            self.update(initial_value)

    def __getitem__(self, key):
        return self.__storage.read(key)

    def __setitem__(self, key, value):
        self.__storage.write(key, value)

    def __iter__(self):
        return self.keys()

    def update(self, dict_):
        for key, value in dict_.items():
            self.__storage.write(key, value)

    def pop(self, key):
        self.remove(key)

    def keys(self):
        return self.__storage.read_key_generator()

    def values(self):
        return self.__storage.read_value_generator()

    def items(self):
        return self.__storage.read_key_value_generator()
