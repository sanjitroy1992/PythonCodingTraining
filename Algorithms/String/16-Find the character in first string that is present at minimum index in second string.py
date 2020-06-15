"""
Given a string str and another string patt. Find the character in patt that is present at the minimum index in str. If no character of patt is present in str then print ‘No character present’.

Examples:

Input: str = “geeksforgeeks”, patt = “set”
Output: e
Both e and s of patt are present in str,
but e is present at minimum index, which is 1.

Input: str = “adcffaet”, patt = “onkl”
Output: No character present
"""


# first that is present at minimum index
# in second String

# function to find the minimum index character
def printMinIndexChar(Str, patt):
    # to store the index of character having
    # minimum index
    minIndex = 10 ** 9
    print(minIndex)
    # lengths of the two Strings
    m = len(Str)
    n = len(patt)

    # traverse 'patt'
    for i in range(n):

        # for each character of 'patt' traverse 'Str'
        for j in range(m):

            # if patt[i] is found in 'Str', check if
            # it has the minimum index or not. If yes,
            # then update 'minIndex' and break
            if (patt[i] == Str[j] and j < minIndex):
                minIndex = j
                break
    print(minIndex)

    # print the minimum index character
    if (minIndex != 10 ** 9):
        print("Minimum Index Character = ", Str[minIndex])

        # if no character of 'patt' is present in 'Str'
    else:
        print("No character present")

    # Driver code


Str = "geeksforgeeks"
patt = "set"
printMinIndexChar(Str, patt)