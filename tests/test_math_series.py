from math_series import __version__
from math_series.series import fibonacci
from math_series.series import fibonacci_iteration

def test_version():
    assert __version__ == '0.1.0'


def test_fib_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fib_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fib_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fib_theree():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_fib_four():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected

def test_fib_five():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_fib_six():
    actual = fibonacci(6)
    expected = 8
    assert actual == expected


def test_fib_iteration_zero():
    actual = fibonacci_iteration(0)
    expected = 0
    assert actual == expected

def test_fib_iteration_one():
    actual = fibonacci_iteration(1)
    expected = 1
    assert actual == expected

def test_fib_iteration_two():
    actual = fibonacci_iteration(2)
    expected = 1
    assert actual == expected

def test_fib_iteration_three():
    actual = fibonacci_iteration(3)
    expected = 2
    assert actual == expected

def test_fib_iteration_four():
    actual = fibonacci_iteration(4)
    expected = 3
    assert actual == expected

def test_fib_iteration_five():
    actual = fibonacci_iteration(5)
    expected = 5
    assert actual == expected

def test_fib_iteration_six():
    actual = fibonacci_iteration(6)
    expected = 8
    assert actual == expected

def test_fib_iteration_seven():
    actual = fibonacci_iteration(7)
    expected = 13
    assert actual == expected







