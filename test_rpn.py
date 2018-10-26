import unittest
import rpn

# Comment is back

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)

    def test_sub(self):
        result = rpn.calculate("4 3 -")
        self.assertEqual(1, result)

    def test_toomany(self):
        with self.assertRaises(ValueError):
            result = rpn.calculate('1 2 3 +')
    def test_exponential(self):
        result = rpn.calculate('2 3 ^')
        self.assertEqual(8, result)

if __name__ == '__main__':
    unittest.main()
