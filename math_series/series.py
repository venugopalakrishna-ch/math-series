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

def lucas_recursive(n):
    if n == 1:
        return 2
    elif n == 2:
        return 1
    elif n == 0:
        return n
    else:
        return lucas_recursive(n-1) + lucas_recursive(n-2)

def lucas_iterative(n):
    count = 2    
    n1 = 2
    n2 = 1
    if n > 2:
        while count < n:
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        return nth
    else:
        if n == 1:
            return 2
        elif n == 2:
            return 1
        elif n == 0:
            return n

def sum_series(n,default1="",default2=""):
    if n == 0:
        return n
    elif default1 != "" and default2 != "":
        if n == 1:  
            return 2
        elif n == 2 :
            return 1
        else:
            return sum_series(n-1,2,1) + sum_series(n-2,2,1)
    elif n== 1:
         return n  
    else:
        return sum_series(n-1) + sum_series(n-2)   
  



