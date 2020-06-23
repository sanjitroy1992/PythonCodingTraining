"""
Given a sorted array and a number x, find the pair in array whose sum is closest to x
Examples:

Input: arr[] = {10, 22, 28, 29, 30, 40}, x = 54
Output: 22 and 30

Input: arr[] = {1, 3, 4, 7, 10}, x = 15
Output: 4 and 10

Note: Here taking the absolute value of the difference is very important. this way we could check the posi
"""
import sys


def printClosest(arr, n, x):
    # To store indexes of result pair
    res_l, res_r = 0, 0

    # Initialize left and right indexes
    # and difference between
    # pair sum and x
    l, r, diff = 0, n - 1, sys.maxsize

    # While there are elements between l and r
    while r > l:
        # Check if this pair is closer than the
        # closest pair so far
        if abs(arr[l] + arr[r] - x) < diff:
            res_l = l
            res_r = r
            diff = abs(arr[l] + arr[r] - x)

        if arr[l] + arr[r] > x:
            # If this pair has more sum, move to
            # smaller values.
            r -= 1
        else:
            # Move to larger values
            l += 1

    print('The closest pair is {} and {}'
          .format(arr[res_l], arr[res_r]))

if __name__ == "__main__":
    # arr = [10, 22, 28, 29, 30, 40]
    arr = [-2,-1,0,2,3]
    n = len(arr)
    x=1
    printClosest(arr, n, x)

def printClosestTwoArray(arr1, arr2, target):
    n = len(arr1)
    m = len(arr2)
    diff = sys.maxsize
    l = 0
    r = m-1
    while(l<n and r>=0):
        if abs(arr1[l] +arr2[r] -target) <diff:
            diff = abs(arr1[l] +arr2[r] -target)
            res_l = l
            res_r = r
        if arr1[l] +arr2[r] > target:
            r -= 1
        else:
            l += 1
    print('The closest pair is {} and {}'
          .format(arr1[res_l], arr2[res_r]))
# Driver code to test above
if __name__ == "__main__":
    # arr = [10, 22, 28, 29, 30, 40]
    # n = len(arr)
    # x = 54
    # printClosest(arr, n, x)

    ar1 = [1, 4, 5, 7]
    ar2 = [10, 20, 30, 40]
    x = 45
    printClosestTwoArray(ar1, ar2, x)