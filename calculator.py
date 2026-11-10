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

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a   # raise ZeroDivisionError if a == 0

def log(a, b):
    # use math library + raise ValueError
    if a <= 0:
        raise ValueError('negative value')
    return math.log(a, b)

def exp(a, b):
    return a**b
