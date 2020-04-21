"""
Given an array nums, write a func to move all 0's to the end of it while maintaining the relative order or the
non zero elements.

Example:
    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]
"""

def move_zero():
    nums = [0, 1, 0, 3, 12]
    zerolist = []
    numlist = []
    if len(nums) == 0:
        return False
    for i in range(len(nums)):
        if nums[i] == 0:
            zerolist.append(nums[i])
        else:
            numlist.append(nums[i])
    return numlist + zerolist

# print(move_zero())

"""
Solution2: 
[0, 1, 0, 3, 12]
Let's take two pointers i and j
Swap num[i] and num[j] when i is not a non zero value
then increase j if you are swapping num[i] and num[j]
"""
nums = [0, 1, 0, 3, 12]
j = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[j], nums[i] = nums[i], nums[j]
        j += 1
print(nums)
