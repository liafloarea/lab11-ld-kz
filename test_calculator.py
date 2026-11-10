import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(3, add(1,2))
        self.assertEqual(4, add(6, -2))
        self.assertEqual(10, add(0, 10))

    def test_subtract(self): # 3 assertions
        self.assertEqual(4, subtract(6, 2))
        self.assertEqual(3, subtract(1, -2))
        self.assertEqual(-10, subtract(0, 10))

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(2, mul(2, 2))
        self.assertEqual(10, mul(5, 2))
        self.assertEqual(-2, mul(2, -1))

    def test_divide(self): # 3 assertions
        self.assertEqual(2, div(4, 2))
        self.assertEqual(4, div(12, 3))
        self.assertEqual(-2, div(4, -2))

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(4, log(16, 2))
        self.assertEqual(3, log(27, 3))
        self.assertEqual(2, log(16, 4))

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(-2, 0)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-1, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(4, hypotenuse(4, 2))
        self.assertEqual(13, hypotenuse(5, 12))
        self.assertEqual(17, hypotenuse(8, 15))

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-9)
        self.assertEqual(9, sqrt(9, 2))
        self.assertEqual(25, sqrt(5, 2))
        self.assertEqual(64, sqrt(8, 2))

# Do not touch this
if __name__ == "__main__":
    unittest.main()