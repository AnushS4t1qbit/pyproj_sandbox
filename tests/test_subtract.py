import unittest

from calculat0r.subtract import Subtract

class SubtractTest(unittest.TestCase):

    def test_subtract(self):
        subtract = Subtract()

        self.assertEqual(subtract(99, 54), 45)

    def test_subtract_by_zero(self):
        subtract = Subtract()

        self.assertEqual(subtract(9, 0), 9)

    def test_invalid_input(self):
        subtract = Subtract()

        with self.assertRaises(TypeError):
            subtract(0.1, 1) # float

        with self.assertRaises(TypeError):
            subtract('a', 1) # string

    def test_subtract_by_negative(self):
        subtract = Subtract()

        self.assertEqual(subtract(9, -1), 10)

    def test_subtract_two_negatives(self):
        subtract = Subtract()

        self.assertEqual(subtract(-9, -1), -8)

if __name__ == '__main__':
    unittest.main()
