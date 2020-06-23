"""
Given an array A of integers, return max value in the mountain array.

Example 1:
Input: [1,2,1]
Output: 2

Example 2:
Input: [3,5,5,4]
Output: 5

Example 3:
Input: [0,3,2,1]
Output: 3
"""
def find_peak(arr):
    low = 0
    high = len(arr)-1
    while(low<high):
        mid = low + (high-low)//2
        if (arr[mid] < arr[mid+1]):
            low = mid + 1
        else:
            high = mid
    return arr[low]

print(find_peak([0,3,2,1,3,4,5,7,8,5,6,9,2]))