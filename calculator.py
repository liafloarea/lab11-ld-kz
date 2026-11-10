"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def square_root(a):
    # raise ValueError if a < 0
    if a < 0:
        raise ValueError('negative value')
    return math.sqrt(a)

def hypotenuse(a, b):
    # can have negative nums
    returnmath.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a   # raise ZeroDivisionError if a == 0

<<<<<<< HEAD
def log(a, b): # raise
    if a <= 0 or b <= 0:
        raise ValueError
    return logarithm(a, b)# use math library/raise ValueError

def exp(a, b):
    return a ** b

def logarithm(a, b):
    # use math library + raise ValueError
    if a <= 0:
        raise ValueError('negative value')
    return math.log(a, b)

def exponent(a, b):
    return a**b
