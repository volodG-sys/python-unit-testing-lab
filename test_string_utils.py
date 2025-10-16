import unittest
from string_utils import reverse_string, count_words, unique_values

class TestStringUtils(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("Python"), "nohtyP")

    def test_count_words(self):
        self.assertEqual(count_words("Unit testing is great"), 4)

    def test_unique_values(self):
        result = unique_values([1, 2, 2, 3, 3, 3])
        self.assertCountEqual(result, [1, 2, 3])

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            reverse_string(123)
