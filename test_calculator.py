import calculator
from math import factorial
import numpy as np

#Project 0, IN1910 - Iris Bore
#Exercise 1
def test_add():
    s = 3
    assert s == calculator.add(2,1)

#Exercise 2
def test_float_add():
    s = 0.3
    tol = 1e-10
    assert abs(s - calculator.add(0.1, 0.2)) < tol

#Exercise 3
def test_string_add():
    s = 'Hello World'
    assert s == calculator.add('Hello ', 'World')

#Exercise 4
def test_factorial():
    est = calculator.factorial(10)
    ex = factorial(10)
    assert est == ex

def test_sin():
    est = calculator.sin(np.pi/2, 10)
    ex = 1
    tol = 1e-10
    assert abs(est - ex) < tol

def test_divide():
    est = calculator.divide(4,2)
    ex = 4/2
    assert est == ex

def test_square():
    est = calculator.square(2)
    ex = 2**2
    assert est == ex

def test_squareroot():
    est = calculator.squareroot(4)
    ex = np.sqrt(4)
    assert est == ex

#Exercise 5
import pytest

def test_if_adding_string_value_raises_Type_Error():
    with pytest.raises(TypeError):
        calculator.add('Hello', 1)

def test_if_divide_by_0__raises_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(1,0)

#Exercise 6
@pytest.mark.parametrize(
    "arg, expected_output", [[(-1, -1), -2], [(1, 1), 2], [(1, 0), 1]])
def test_add(arg, expected_output):
    assert calculator.add(arg[0], arg[1]) == expected_output


@pytest.mark.parametrize(
    "arg, expected_output", [[(0.1, 0.2), 0.3], [(0.4, 0.5), 0.9],
                            [(0.3, 1.4), 1.7]])

def test_float_add(arg, expected_output):
    assert calculator.add(arg[0], arg[1]) - expected_output < 1e-10


@pytest.mark.parametrize(
    "arg, expected_output", [[(-1, -1), -2], [(1, 1), 2], [(1, 0), 1]])
def test_string_add(arg, expected_output):
    assert calculator.add(arg[0], arg[1]) == expected_output


@pytest.mark.parametrize("arg, expected_output", [(1,1),(0,1),(2,2),(3,6)])
def test_factorial(arg, expected_output):
    assert calculator.factorial(arg) == expected_output


@pytest.mark.parametrize(
    "arg, expected_output", [[(0, 10), 0], [(3*np.pi/2, 10), -1],
    [(np.pi, 10), 0]])
def test_sin(arg, expected_output):
    assert abs(calculator.sin(arg[0], arg[1]) - expected_output) < 1e-5


@pytest.mark.parametrize(
    "arg, expected_output", [[(-1, -1), 1], [(4, 2), 2], [(12, 3), 4]])
def test_divide(arg, expected_output):
    assert calculator.divide(arg[0], arg[1]) == expected_output


@pytest.mark.parametrize("x, x2", [(0, 0), (1, 1), (2, 4), (3, 9)])
def test_square(x, x2):
    assert calculator.square(x) == x2


@pytest.mark.parametrize("x, sqrtx", [(0, 0), (1, 1), (4, 2), (9, 3)])
def test_squareroot(x, sqrtx):
    assert calculator.squareroot(x) == sqrtx
