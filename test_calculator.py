import unittest
import calculator

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
def test_multiply(self): # 3 assertions
    self.assertEquals(calculator.mul(45, 0), 0)
    self.assertEquals(calculator.mul(45, 1), 45)
    self.assertEquals(calculator.mul(6, 9), 72)

def test_divide(self): # 3 assertions
    self.assertNone(calculator.div(45/0))
    self.assertEquals(calculator.div(6/3), 2)
    self.assertEquals(calculator.div(6/1), 1)

    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    with self.assertRaises(ValueError):
        calculator.logarithm(0, 5)
    #     fill in code

def test_hypotenuse(self): # 3 assertions
    self.assertEquals(calculator.hypotenuse(3,4), 5)
    self.assertEquals(calculator.hypotenuse(-3, -4), 5)
    self.assertEquals(calculator.hypotenuse(6, 8), 10)

def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    with self.assertRaises(ValueError):
        calculator.square_root(-4)
    self.assertEquals(calculator.square_root(4), 2)
    self.assertEquals(calculator.square_root(9), 3)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()