import unittest

from extended_collections import FixedKeysDict
from extended_collections.fixed_keys_dict import FixedKeysDictObject


class FixedKeysDictTests(unittest.TestCase):
    def test_create(self):
        Point = FixedKeysDict("Point", ['x', 'y'])
        self.assertIsInstance(Point, FixedKeysDict)

    def test_create_object(self):
        Point = FixedKeysDict("Point", ['x', 'y'])
        object = Point.object()
        self.assertIsInstance(object, FixedKeysDictObject)


if __name__ == "__main__":
    unittest.main()