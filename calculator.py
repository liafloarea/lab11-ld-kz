import math
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # raise ZeroDivisionError if a == 0
    if a == 0:
        raise ZeroDivisionError('division by zero')
    return b / a

def logarithm(a, b):
    # use math library + raise ValueError
    if a <= 0:
        raise ValueError('negative value')
    return math.log(a, b)

def exponent(a, b):
    return a**b
