import unittest

from calculat0r.add import Add

class AddTest(unittest.TestCase):

    def test_add(self):
        add = Add()

        self.assertEqual(add( 1, 2), 3)  # regular positive numbers
        self.assertEqual(add(-1, 9), 8)  # handle negative numbers
        self.assertEqual(add( 0, 0), 0)  # zero case

    def test_invalid_input(self):
        add = Add()

        with self.assertRaises(TypeError):
            add(0.1, 1) # float

        with self.assertRaises(TypeError):
            add('a', 1) # string

if __name__ == '__main__':
    unittest.main()
