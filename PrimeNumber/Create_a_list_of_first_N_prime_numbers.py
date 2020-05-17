"""
Python script to create a list of first N prime numbers
"""
def next_prime_number(num):
    while True:
        num += 1
        for i in range(2, num):
            if num%2 == 0:
                break
        else:
            return num

def prime_number_producer(N):
    num, count = 1, 1
    while(count<=N):
        num = next_prime_number(num)
        yield num
        count += 1


N = int(input("How many prime numbers you want to generate: "))
l = [i for i in prime_number_producer(N)]
print(l)