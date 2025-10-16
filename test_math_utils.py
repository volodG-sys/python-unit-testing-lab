import unittest
from math_utils import add, subtract, divide

class TestMathUtils(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 7), 12)

    def test_subtract(self):
        self.assertEqual(subtract(10, 3), 7)

    def test_divide(self):
        self.assertAlmostEqual(divide(9, 3), 3.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
