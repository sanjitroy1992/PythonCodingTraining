"""
Reverse a number

"""

def reverse(x: int) -> int:
    rev = 0
    temp = x
    x = abs(x)
    while (x > 0):
        rem = x % 10
        x = x // 10
        rev = rem + (rev * 10)
    print(temp)
    print((2**31)-1)
    if (temp >= (2**31)-1 or
            temp <= -(2**31)-1):
        return 0
    if temp<0:
        return 0-rev
    else:
        return rev

print(reverse(1534236469))


def reverse(seq):
    """Reverses elements of a list."""
    for i in range(len(seq)//2):
        x = seq[i]
        y = seq[-i-1]
        seq[i] = y
        seq[-i-1] = x

l = ['a', 'b', 'c', 'd', 'e']
# print(reverse(l))
# print(l)

print(l[0:-1])