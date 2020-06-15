"""
1. Generate all prime numbers which are there within N number
let's say if n = 10
output = 2, 3, 5, 7
"""
def generate_prime_numbers_within_a_range():
    number = int(input("Enter the range value to generate prime numbers: "))
    list1 = []
    for n in range(2, number+1):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            list1.append(str(n))
    print(', '.join(list1))

# generate_prime_numbers_within_a_range()

"""
2. Generate first N prime numbers

Approach:
- From user input get the number of primary numbers to be generated
- create a function to generate prime numbers for a range where max is sys.maxsize
- there will be two for loop one is outer and one is inner
- inside the inner for loop we'll generate a prime number and add it to a list and increment the counter
- inside the outer for loop we'll put a condition to check if the user input matches with the counter then we have generaed maximum prime numbers.
- finally brake the outer for loop.
"""
import sys
def prime_number_for_n_values():
    number = int(input("Enter the number of prime numbers you want to generate: "))
    count = 0
    list1 = []
    for n in range(2, sys.maxsize):
        if count == number:
            break
        for i in range(2,n):
            if n%i == 0:
                break
        else:
            list1.append(str(n))
            count += 1
    print(', '.join(list1))

# prime_number_for_n_values()


