import unittest

from calculat0r.multiply import Multiply

class MultiplyTest(unittest.TestCase):

    def test_multiply(self):
        multiply = Multiply()

        self.assertEqual(multiply( 4, 6), 24)

    def test_multiply_by_zero(self):
        multiply = Multiply()

        self.assertEqual(multiply(9, 0), 0)
        self.assertEqual(multiply(0, 8), 0)

    def test_invalid_input(self):
        multiply = Multiply()

        with self.assertRaises(TypeError):
            multiply(0.1, 1) # float

        with self.assertRaises(TypeError):
            multiply('a', 1) # string

    def test_multiply_by_negative(self):
        multiply = Multiply()

        self.assertEqual(multiply(9, -1), -9)

    def test_multiply_two_negatives(self):
        multiply = Multiply()

        self.assertEqual(multiply(-9, -1), 9)

if __name__ == '__main__':
    unittest.main()
