import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(45, 0), 0)
        self.assertEqual(mul(45, 1), 45)
        self.assertEqual(mul(6, 9), 72)

    def test_divide(self): # 3 assertions
        assert div(45/0) is None
        self.assertEqual(div(6/3), 2)
        self.assertEqual(div(6/1), 1)

    # ##########################

    ######## Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5,1),4)
        self.assertEqual(subtract(111,110),1)
        self.assertNotEqual(subtract(20,20),1)

    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        #     # call log function inside, example:
        #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(0, 5)
        #     fill in code

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertEqual(hypotenuse(-3, -4), 5)
        self.assertEqual(hypotenuse(6, 8), 10)

    def test_sqrt(self): # 3 assertions
        #     # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(9), 3)
        #     # Test basic function
        #     fill in code
        ##########################

    ####### Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(0,5)
    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(8,3),2)
        self.assertEqual(logarithm(9,2),3)
        self.assertEqual(logarithm(100,2),10)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        self.assertRaises(ValueError)
            logarithm(0,5)



# Do not touch this
if __name__ == "__main__":
    unittest.main()