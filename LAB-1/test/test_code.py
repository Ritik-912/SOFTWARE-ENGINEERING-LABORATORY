# test_math_functions.py

import pytest
from sys import path
path.append("../src/")
from source_code import sum, difference, square, cube, divide

def test_sum():
    assert sum(1, 2) == 3
    assert sum(-1, 1) == 0
    assert sum(0, 0) == 0

def test_difference():
    assert difference(1, 2) == -1
    assert difference(-1, 1) == -2
    assert difference(0, 0) == 0

def test_square():
    assert square(1) == 1
    assert square(-1) == 1
    assert square(0) == 0

def test_cube():
    assert cube(1) == 1
    assert cube(-1) == -1
    assert cube(0) == 0

def test_divide():
    assert divide(4, 2) == 2
    assert divide(-4, 2) == -2
    assert divide(0, 1) == 0
    assert divide(4, 0)