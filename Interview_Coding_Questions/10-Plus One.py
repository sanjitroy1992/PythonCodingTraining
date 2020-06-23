"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""

def plus_one(arr):
    if len(arr) == 0:  # empty string as input
        arr = [1]
    elif (arr[-1] == 9):  # if last digit is 9
        arr = plus_one(arr[:-1]) # add 1 to the digit before the last one, i.e. 0 to N-2 index
        print(f"before: {arr}")
        arr.extend([0])   # add 0 at the end
        print(f"after: {arr}")
    else:
        print("before +1: {}".format(arr))
        arr[-1] += 1  # case where last digit is not 9, just add 1
        print("after +1: {}".format(arr))
    return arr

print(plus_one([1,2,9]))