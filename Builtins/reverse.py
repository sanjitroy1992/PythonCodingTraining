"""
Write multiple ways to reverse a string
"""
## Solution 1:

string = 'Python'
## Using for loop
def reverse(s):
    str1 = ''
    for i in range(len(s)):
        str1 = s[i] + str1
    print(str1)
reverse(string)

## Solution 2:
## Using builtin reversed method
lis1 = list(reversed(string))
print("".join(lis1))

## Solution 3:
## Using list slicing
revlist = string[::-1]
print("".join(revlist))

### For a list of values
list1 = ["This", "is", "the", "best", "time"]
reversestring = lambda x: "".join(reversed(x))
lis1 = list(map(reversestring, list1))
print(", ".join(lis1))
