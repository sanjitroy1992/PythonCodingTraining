"""
a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers.
The simplest is the series 1, 1, 2, 3, 5, 8, 13 etc.

fibonacci(5) = 5 -->fibonacci(3) + fibonacci(4)
fibonacci(7) = 13 -->fibonacci(5) + fibonacci(6)

Approaches:
01: Recursive functions are good but for bigger number it takes a lot of computation time!
02: Memoization: In computing, memoization or memoisation is an optimization technique used primarily to speed up
computer programs by storing the results of expensive function calls and returning the cached result when the same
inputs occur again.
03: Capitalizing Memoization approach let use now use the inbuilt decorator lru.
lru_cache--> Least Recently Used Cache
"""
# 01 approach: recursion method:
from functools import lru_cache
def fibonacci_recursion(n):
    if type(n) != int:
        raise AssertionError("n must be a positive integer")
    elif n <= 0:
        raise AssertionError("n must be a positive integer greater than 0")
    else:
        if n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

# print(fibonacci_recursion(7))


##02 approach: Memoization
fibonacci_cache = {}
def fibonacci_memoization(n):
    ## If we have cache value then return it
    # print(fibonacci_cache)
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    ## Compute the Nth term
    if type(n) != int:
        raise AssertionError("n must be a positive integer")
    elif n <= 0:
        raise AssertionError("n must be a positive integer greater than 0")
    else:
        if n == 1:
            return 1
        elif n == 2:
            return 1
        elif n > 2:
            value = fibonacci_memoization(n-1) + fibonacci_memoization(n-2)
        # cache the value and return it
        fibonacci_cache[n] = value
        print(fibonacci_cache)

        return value

for i in range(1, 6):
    print("{}: {}".format(i, fibonacci_memoization(i)))

##03 approach: lru
@lru_cache(maxsize=1000)
def fibonacci_lru_cache(n):
    ## Compute the Nth term
    if type(n) != int:
        raise AssertionError("n must be a positive integer")
    elif n <= 0:
        raise AssertionError("n must be a positive integer greater than 0")
    else:
        if n == 1:
            return 1
        elif n == 2:
            return 1
        elif n > 2:
            return fibonacci_memoization(n - 1) + fibonacci_memoization(n - 2)

# for i in range(1, 500):
#     print("{}: {}".format(i, fibonacci_lru_cache(i)))



