"""

Repeated Character Whose First Appearance is Leftmost
Given a string, find the repeated character present first in the string.

Examples:

Input  : geeksforgeeks
Output : g
(mind that it will be g, not e.)

Input  : abcdabcd
Output : a

Input  : abcd
Output : -1
No character repeats
Asked in: Goldman Sachs internship


How to solve this problem using one traversal of input string?

Method 1 (Traversing from Left to Right) We traverse the string from left to right. We keep track of the leftmost index of every character. If a character repeats, we compare its leftmsot index with current result and update the result if result is greater
"""

# Python 3 program to find first repeating
# character
import sys

NO_OF_CHARS = 256

# The function returns index of the first
# repeating character in a string. If
# all characters are repeating then
# returns -1 */
def firstRepeating(str1):
    first_index=[-1 for i in range(NO_OF_CHARS)]
    n= len(str1)
    res=sys.maxsize
    for i,letter in enumerate(str1) :
        if first_index[ord(letter)]==-1:
            first_index[ord(letter)]=i
        else:
            res=min(res,first_index[ord(letter)])
    if res==sys.maxsize:
        return -1
    else:
        return res





# Driver function
if __name__ == '__main__':
    str = "geeksforgeeks"
    index = firstRepeating(str)
    if (index == -1):
        print("Either all characters are distinct or string is empty")
    else:
        print("First Repeating character is",str[index])



