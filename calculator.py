#https://github.com/CtrlAubDel/lab11-AC-MSG

# Partner 1: Aubrey Corcoran
# Partner 2: Mariana Silva Gomez

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    if a < 0:
        raise ValueError
    else:
        return math.sqrt(a)
    
def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    pass
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Can't divide by 0.")
    else:
        return a // b

def logarithm(a, b):
    
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