"""
Input:   str = "a,b$c"
Output:  str = "c,b$a"
Note that $ and , are not moved anywhere.
Only subsequence "abc" is reversed

Input:   str = "Ab,c,de!$"
Output:  str = "ed,c,bA!$"

Simple Solution:
1) Create a temporary character array say temp[].
2) Copy alphabetic characters from given array to temp[].
3) Reverse temp[] using standard string reversal algorithm.
4) Now traverse input string and temp in a single loop. Wherever there is alphabetic character is input string, replace it with current character of temp[].

Efficient Solution:
Time complexity of above solution is O(n), but it requires extra space and it does two traversals of input string.
We can reverse with one traversal and without extra space. Below is algorithm.

1) Let input string be 'str[]' and length of string be 'n'
2) l = 0, r = n-1
3) While l is smaller than r, do following
    a) If str[l] is not an alphabetic character, do l++
    b) Else If str[r] is not an alphabetic character, do r--
    c) Else swap str[l] and str[r]
"""
string1 = "ab$cd"
def reverse_string(string1):
    l = 0
    r = len(string1)-1
    toList = list(string1)
    while(l<r):
        if not str(toList[l]).isalpha():
            l += 1
        if not str(toList[r]).isalpha():
            r -= 1
        else:
            toList[l], toList[r] = toList[r], toList[l]
            l += 1
            r -= 1
    return ''.join(toList)

print(reverse_string(string1))