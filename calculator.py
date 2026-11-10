import math
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    # raise ZeroDivisionError if a == 0
    if a == 0:
        raise ZeroDivisionError('division by zero')
    return b / a

def log(a, b):
    # use math library + raise ValueError
    if a <= 0:
        raise ValueError('negative value')
    return math.log(a, b)

def exp(a, b):
    return a**b
