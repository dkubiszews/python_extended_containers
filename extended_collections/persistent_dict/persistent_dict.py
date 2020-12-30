# TODO: add copyrights

import pickle

from extended_collections.persistent_dict.sqlite_storage import SQLiteStorage


class PersistentDict:
    """
    Dict stored on disk.
    """

    def __init__(self, storage_path, initial_dict=None):
        self.__storage = SQLiteStorage(storage_path)
        self.__storage.open()

        if initial_dict is not None:
            if not isinstance(initial_dict, dict):
                raise TypeError("The 'initial_value' must be dict type")
            self.update(initial_dict)

    def __getitem__(self, key):
        return pickle.loads(self.__storage.read(key))

    def __setitem__(self, key, value):
        self.__storage.write(key, pickle.dumps(value))

    def __iter__(self):
        return self.keys()

    def update(self, dict_):
        for key, value in dict_.items():
            self.__storage.write(key, pickle.dumps(value))

    def pop(self, key):
        self.__storage.remove(key)

    def keys(self):
        return self.__storage.read_key_generator()

    def values(self):
        for value in self.__storage.read_value_generator():
            yield pickle.loads(value)

    def items(self):
        for key, value in self.__storage.read_key_value_generator():
            yield key, pickle.loads(value)
