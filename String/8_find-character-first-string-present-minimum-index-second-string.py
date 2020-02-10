"""

Find the character in first string that is present at minimum index in second string
Given a string str and another string patt. Find the character in patt that is present at the minimum index in str. If no character of patt is present in str then print ‘No character present’.

Examples:

Input: str = “geeksforgeeks”, patt = “set”
Output: e
Both e and s of patt are present in str,
but e is present at minimum index, which is 1.

Input: str = “adcffaet”, patt = “onkl”
Output: No character present

"""

# Python3 implementation to find the character in
# first that is present at minimum index
# in second String
import sys
# function to find the minimum index character
def printMinIndexChar(str1, patt):
    n_str1=len(str1)
    n_pat=len(patt)
    min_index= sys.maxsize
    for i in range(n_pat):
        for j in range(n_str1):
            if(patt[i]==str1[j] and j<min_index):
                min_index=j
                break

    if min_index==sys.maxsize:
        print("No character present")
    else:
        print("Minimum index character is {}".format(str1[min_index]))


# Driver code

Str = "geeksforgeeks"
patt = "set"
printMinIndexChar(Str, patt)