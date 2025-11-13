# https://github.com/mvsg2311-web
# Partner 1: Aubrey Corcoran
# Partner 2: Mariana Silva Gomez

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Can't divide by 0.")
    else:
        return a // b

def log(a, b):

    if a <= 0:
        raise ValueError("A can not be less than 0.")
        return
    if b <= 1:
        raise ValueError("B must be greater than 1.")
        return
    else:
        return math.log(a, b)

def exp(a, b):
    return a ** b
