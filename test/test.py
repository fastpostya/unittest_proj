import unittest
from utils.arrs import get, my_slice


class TestMyFunc(unittest.TestCase):
    def test_get(self):
        self.assertEqual(get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(get([], 0, "test"), "test")
        self.assertEqual(get([], -1, "test"), "test")
        self.assertIsNone(get([], -1))

    def test_slice(self):
        self.assertEqual(my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(my_slice([1, 2, 3, 2, 8], 1, -1), [2, 3, 2])
        self.assertEqual(my_slice([1, 2, 3, 2, 8], -3, -1), [3, 2])
        self.assertEqual(my_slice([1, 2, 3], 4, 6), [])
        self.assertEqual(my_slice([1, 2, 3, 4], 3, 1), [])
        self.assertEqual(my_slice([], 1, 1), [])
        self.assertEqual(my_slice([1, 2, 3, 2, 8], -6, -1), [1, 2, 3, 2])

