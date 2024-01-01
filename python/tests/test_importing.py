import unittest
from my_module import sub_numbers

class TestMyModule(unittest.TestCase):

    def test_sub_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, -1)

    def test_sub_numbers_negative(self):
        result = add_numbers(-2, 3)
        self.assertEqual(result, -4)

    def test_sub_numbers_zero(self):
        result = add_numbers(0, 0)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()