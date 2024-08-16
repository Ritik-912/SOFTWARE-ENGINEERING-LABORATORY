'''
This script contains various python functions that will be tested using pytest.
'''
def sum(a: int, b:int) -> int:
    return a+b

def difference(a: int, b:int) -> int:
    return a-b

def square(a: int) -> int:
    return a**2

def cube(a: int) -> int:
    return a**3

def divide(a: int, b: int) -> int:
    if b!=0:
        return a//b
    else:
        return a