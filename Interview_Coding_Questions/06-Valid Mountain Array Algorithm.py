"""
Given an array A of integers, return true if and only if it is a valid mountain array.

Example 1:
Input: [2,1]
Output: false

Example 2:
Input: [3,5,5]
Output: false

Example 3:
Input: [0,3,2,1]
Output: true
"""
def mountain(arr):
    N = len(arr)
    l = 0
    r = 0
    peak = 0
    while(peak<N-1 and arr[peak] <=arr[peak +1]):
        peak += 1
        l += 1
    while(peak<N-1 and arr[peak]> arr[peak+1]):
        peak += 1
        r += 1
    if (peak == N-1 and (l*r)>0):
        print("It's a mountain array")
    else:
        print("It's not a mountain array")

mountain([0,3,2,1])
mountain([3,5,5])
mountain([2, 1])
mountain([-1,0,2,1])
mountain([0,1,2,2,2,1,0])