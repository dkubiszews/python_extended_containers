# TODO: add copyrights

class FixedKeysDictObject:
    def __init__(self, name, dict_):
        self.__name = name
        self.__dict = dict_

    def __getitem__(self, key):
        return self.__dict[key]

    def __setitem__(self, key, value):
        if key not in self.__dict:
            raise KeyError(key)

        self.__dict[key] = value

    def __getattr__(self, attr):
        return self.__dict[attr]


class FixedKeysDict:
    def __init__(self, name, keys):
        self.__name = name
        self.__dict = {key: None for key in keys}

    def object(self, **kwargs):
        dict_copy = self.__dict.copy()

        for key, value in kwargs.items():
            if key not in dict_copy:
                raise KeyError(key)
            dict_copy[key] = value

        return FixedKeysDictObject(self.__name, dict_copy)