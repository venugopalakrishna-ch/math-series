from math_series import __version__
from math_series.series import fibonacci
from math_series.series import fibonacci_iteration
from math_series.series import lucas_recursive
from math_series.series import lucas_iterative
from math_series.series import sum_series

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

def test_lucas_recursiv_zero():
    assert lucas_recursive(0) == 0

def test_lucas_recursiv_one():
    assert lucas_recursive(1) == 2

def test_lucas_recursiv_two():
    assert lucas_recursive(2) == 1

def test_lucas_recursiv_three():
    assert lucas_recursive(3) == 3

def test_lucas_recursiv_four():
    assert lucas_recursive(4) == 4

def test_lucas_recursiv_five():
    assert lucas_recursive(5) == 7

def test_lucas_recursiv_six():
    assert lucas_recursive(6) == 11

def test_lucas_iterative_zero():
    assert lucas_iterative(0) == 0

def test_lucas_iterative_one():
    assert lucas_iterative(1) == 2

def test_lucas_iterative_two():
    assert lucas_iterative(2) == 1

def test_lucas_iterative_three():
    assert lucas_iterative(3) == 3

def test_lucas_iterative_four():
    assert lucas_iterative(4) == 4

def test_lucas_iterative_five():
    assert lucas_iterative(5) == 7

def test_lucas_iterative_six():
    assert lucas_iterative(6) == 11

def test_sum_series_fib_zero():
    assert sum_series(0) == 0

def test_sum_series_fib_one():
    assert sum_series(1) == 1

def test_sum_series_fib_two():
    assert sum_series(2) == 1

def test_sum_series_fib_three():
    assert sum_series(3) == 2

def test_sum_series_fib_four():
    assert sum_series(4) == 3

def test_sum_series_fib_five():
    assert sum_series(5) == 5

def test_sum_series_fib_six():
    assert sum_series(6) == 8

def test_sum_series_lucas_zero():
    assert sum_series(0,2,1) == 0

def test_sum_series_lucas_one():
    assert sum_series(1,2,1) == 2

def test_sum_series_lucas_two():
    assert sum_series(2,2,1) == 1

def test_sum_series_lucas_three():
    assert sum_series(3,2,1) == 3

def test_sum_series_lucas_four():
    assert sum_series(4,2,1) == 4

def test_sum_series_lucas_five():
    assert sum_series(5,2,1) == 7

def test_sum_series_lucas_six():
    assert sum_series(6,2,1) == 11