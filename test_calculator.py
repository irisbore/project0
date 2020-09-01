from calculator import *
import math as m

def test_add():
    s = 3
    assert s == add(2,1)

def test_float_add():
    s = 0.3
    tol = 1e-10
    assert s - add(0.1, 0.2) < tol


def test_string_add():
    s = 'Hello World'
    assert s == add('Hello ', 'World')

def test_factorial():
    est = factorial(10)
    comp = m.factorial(10)
    assert est == comp
