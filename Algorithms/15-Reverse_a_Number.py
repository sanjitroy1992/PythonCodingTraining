"""
Reverse a number

"""
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