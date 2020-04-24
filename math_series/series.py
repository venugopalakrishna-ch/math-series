def fibonacci(n):
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)

    return n

def fibonacci_iteration(n):
    count = 1
    nth = 1
    n1 = 0
    n2 = 1
    if n >= 1:
        while count < n:
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        return nth
    else:
        return n



