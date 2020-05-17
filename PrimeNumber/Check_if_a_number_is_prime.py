"""
A prime number is a positive integer that has exactly two positive integer factors, 1 and itself. It should be greater
than one.
example:
2, 3, 5, 7, 11,13 is a prime number
4, 6, 8, 10 is not a prime number
"""

def prime_number():
    n = int(input("Enter the number to check: "))
    if n < 2:
        print("Not a prime number")
    else:
        for i in range(2, n):
            if n % i == 0:
                print("Not a prime number")
                break
        else:
            print("Prime Number")

prime_number()