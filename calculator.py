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

def div(a, b):
    if b == 0:
        raise ZeroDivisionError
    else:
        return a / b

def logarithm(a, b):
    
    if b is None:
        raise ValueError
    if a <= 0:
        raise ValueError
    if b <= 1:
        raise ValueError
    return math.log(a, b)

def exp(a, b):
    return a ** b