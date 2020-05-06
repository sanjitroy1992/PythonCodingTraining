"""
How to check if a given number is Fibonacci number?

Input : 8
Output : Yes

Input : 34
Output : Yes

Input : 41
Output : No
Youtube: https://youtu.be/tiiWQJGAr2o
"""
import math


def fibonacci_check():
    n = int(input("Enter the number the check: "))
    # n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both

    x1 = 5 * n * n + 4
    x2 = 5 * n * n - 4
    s1 = int(math.sqrt(x1))
    s2 = int(math.sqrt(x2))
    # Returns true if n is a perferct square else false
    if s1 * s1 == x1:
        return True
    if s2 * s2 == x2:
        return True
    else:
        return False

print(fibonacci_check())