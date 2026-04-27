import unittest
import sys
import os

# чтобы Python видел utils.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import add, subtract


class TestCalculator(unittest.TestCase):

    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract_positive(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_subtract_negative(self):
        self.assertEqual(subtract(-5, -3), -2)


if __name__ == "__main__":
    unittest.main()