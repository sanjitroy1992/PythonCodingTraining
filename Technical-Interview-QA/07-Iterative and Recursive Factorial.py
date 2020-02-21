"""
Q. Write a iterative and recursive function that implements the factorial of a number.

Solution1:
5! = 5 * 4 * 3 * 2 * 1 = 120

Solution2:
5!
5 * 4! = 120
4 * 3! = 24
3 * 2! = 6
2 * 1! = 2
1! = 1
Youtube:https://youtu.be/yUOoJL9_y9M?list=PL5tcWHG-UPH1D-JVSiZI_8I8LPUJtoHdg
"""

def factorial():
    n = int(input("enter the number: "))
    x = 1
    for i in range(n,0,-1):
        x *= i
    print(x)
# factorial()

def rec_fact(n):
    if n <= 1:
        return 1
    else:
        return n * rec_fact(n-1)
print(rec_fact(5))