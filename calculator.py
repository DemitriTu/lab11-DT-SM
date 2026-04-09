"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def square_root(a):
    try:
        b = math.sqrt(a)
        return b
    except ValueError as e:
        raise ValueError

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b

def subtract(a, b):
    return a-b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError as e:
        raise ZeroDivisionError


def logarithm(a, b):
    try:
        c = math.log(b, a)
        return c
    except ValueError as e:
        raise ValueError

def exp(a, b):
    return a ** b




