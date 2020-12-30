import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import os
import tempfile
import unittest

from extended_collections import PersistentDict


class PersistentDictTests(unittest.TestCase):

    def setUp(self):
        self.test_work_dir = tempfile.mkdtemp()
        self.storage_path = os.path.join(self.test_work_dir, "storage.db")

    def test_create(self):
        sut = PersistentDict(self.storage_path)

        self.assertIsInstance(sut, PersistentDict)

    def test_initial_value_is_not_a_dict_raise(self):
        self.assertRaises(TypeError, lambda: PersistentDict(self.storage_path, int()))

    def test_set_item(self):
        sut = PersistentDict(self.storage_path)

        sut["new_key"] = "new item"

    def test_get_item(self):
        expected_item = "expected item"
        key = "new key"
        sut = PersistentDict(self.storage_path)

        sut[key] = expected_item

        self.assertEqual(expected_item, sut[key])

    def test_initial_value_is_retrieved(self):
        expected_dict = {"one": 1, "two": 2, "three": 3, "four": 4}
        sut = PersistentDict(self.storage_path, initial_dict=expected_dict)

        actual_dict = {}
        for key, value in sut.items():
            actual_dict[key] = value

        self.assertDictEqual(expected_dict, actual_dict)

    def test_initial_value_keys_are_retrieved(self):
        expected_dict = {"one": 1, "two": 2, "three": 3, "four": 4}
        sut = PersistentDict(self.storage_path, initial_dict=expected_dict)

        actual_keys_set = set()
        for key in sut.keys():
            actual_keys_set.add(key)

        self.assertSetEqual(set(expected_dict.keys()), actual_keys_set)

    def test_initial_value_values_are_retrieved(self):
        expected_dict = {"one": 1, "two": 2, "three": 3, "four": 4}
        sut = PersistentDict(self.storage_path, initial_dict=expected_dict)

        actual_values_set = set()
        for value in sut.values():
            actual_values_set.add(value)

        self.assertSetEqual(set(expected_dict.values()), actual_values_set)

    def test_initial_value_keys_are_retrieved_directly(self):
        expected_dict = {"one": 1, "two": 2, "three": 3, "four": 4}
        sut = PersistentDict(self.storage_path, initial_dict=expected_dict)

        actual_keys_set = set()
        for key in sut:
            actual_keys_set.add(key)

        self.assertSetEqual(set(expected_dict.keys()), actual_keys_set)

    def test_remove_item(self):
        initial_dict = {"one": 1, "two": 2, "three": 3, "four": 4}
        item_to_remove = "three"
        expected_dict = {"one": 1, "two": 2, "four": 4}
        sut = PersistentDict(self.storage_path, initial_dict=initial_dict)

        sut.pop(item_to_remove)

        actual_values_set = set()
        for value in sut.values():
            actual_values_set.add(value)

        self.assertSetEqual(set(expected_dict.values()), actual_values_set)
