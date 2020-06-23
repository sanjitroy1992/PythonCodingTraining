"""
Given a string and number of rows ‘n’. Print the string formed by concatenating n rows when input string is written in row-wise Zig-Zag fashion.
Examples:

Input: str = "ABCDEFGH"
       n = 2
Output: "ACEGBDFH"
Explanation: Let us write input string in Zig-Zag fashion
             in 2 rows.
A   C   E   G
  B   D   F   H
Now concatenate the two rows and ignore spaces
in every row. We get "ACEGBDFH"

Input: str = "GEEKSFORGEEKS"
       n = 3
Output: GSGSEKFREKEOE
Explanation: Let us write input string in Zig-Zag fashion
             in 3 rows.
G       S       G       S
  E   K   F   R   E   K
    E       O       E
Now concatenate the two rows and ignore spaces
in every row. We get "GSGSEKFREKEOE"
"""

def printZigZagConcat(string, n):
    # Corner Case (Only one row)
    if n == 1:
        print(string)
        return

    # Find length of string
    l = len(string)

    # Create an array of
    # strings for all n rows
    arr = ["" for x in range(l)]

    # Initialize index for
    # array of strings arr[]
    row = 0

    # Travers through
    # given string
    for i in range(l):

        # append current character
        # to current row
        # arr[row] += string[i]
        arr[row] = arr[row] + string[i]

        # If last row is reached,
        # change direction to 'up'
        if row == n - 1:
            down = False

        # If 1st row is reached,
        # change direction to 'down'
        elif row == 0:
            down = True

        # If direction is down,
        # increment, else decrement
        if down:
            row += 1
        else:
            row -= 1

    # Print concatenation
    # of all rows
    # print(arr)
    string1 = ""
    for i in range(n):
        # print(arr[i], end="")
        string1 += arr[i]

    print(string1)



str = "GEEKSFORGEEKS"
n = 3
printZigZagConcat(str, n)