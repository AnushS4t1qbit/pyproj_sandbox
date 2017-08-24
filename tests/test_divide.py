import unittest

from calculat0r.divide import Divide

class DivideTest(unittest.TestCase):

    def test_divide(self):
        divide = Divide()

        self.assertEqual(divide( 27, 9), 3)   # regular positive numbers
        self.assertEqual(divide(-32, 8), -4)  # handle negative numbers

    def test_invalid_input(self):
        divide = Divide()

        with self.assertRaises(TypeError):
            divide(0.1, 1) # float

        with self.assertRaises(TypeError):
            divide('a', 1) # string

    def test_divide_by_zero(self):
        divide = Divide()

        with self.assertRaises(ZeroDivisionError):
            divide(9, 0)

if __name__ == '__main__':
    unittest.main()
