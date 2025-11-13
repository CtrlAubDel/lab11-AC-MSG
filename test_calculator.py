# https://github.com/CtrlAubDel/lab11-AC-MSG
# Partner 1: Aubrey Corcoran
# Partner 2: Mariana Silva

import unittest
from calculator import *
import math


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code
    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################
    def test_subtract(self):  # 3 assertions
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(3, 5), -2)
        self.assertEqual(sub(0, 0), 0)
    ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-4, 5), -20)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-9, 3), -3)
        self.assertAlmostEqual(divide(7, 3), 7/3)
    # ##########################
    ##########################

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)

    # def test_logarithm(self): # 3 assertions
    #     fill in code
    def test_logarithm(self):  # 3 assertions
        self.assertAlmostEqual(log(100, 10), 2.0)
        self.assertAlmostEqual(log(8, 2), 3.0)
        self.assertAlmostEqual(log(math.e, math.e), 1.0)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            log(8, 1)
    ##########################

    def test_log_invalid_base(self):  # 1 assertion
        # invalid base or argument should raise ValueError
        with self.assertRaises(ValueError):
            log(8, 1)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        from calculator import logarithm
        with self.assertRaises(ValueError):
            logarithm(0)
    ##########################

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code
    def test_hypotenuse(self): # 3 assertions
        from calculator import hypotenuse
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(8, 15), 17)

    # def test_sqrt(self): # 3 assertions
    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
        from calculator import square_root
        self.assertEqual(square_root(25), 5)
        with self.assertRaises(ValueError):
            square_root(-9)
        self.assertAlmostEqual(square_root(2), 2**0.5)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()