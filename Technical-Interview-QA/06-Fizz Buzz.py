"""
Q. Given a positive integer, N print all the integers from 1 to N.
Note: For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz"

Now, before we go about it.. let's understand the problem statement clearly.
Let's consider the below examples.

Youtube:https://youtu.be/bS837DTJsTI?list=PL5tcWHG-UPH1D-JVSiZI_8I8LPUJtoHdg
"""

def fizzbuzz():
    n = int(input("enter the list items: "))
    for i in range(1, n+1):
        if (i%3==0) and (i%5==0):
            print("FizzBuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)
fizzbuzz()