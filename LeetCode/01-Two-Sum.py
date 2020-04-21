"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
list1 = [2, 7, 11, 15]
target = 9

def two_numbers():
    dict1 = {}
    for i in range(len(list1)):
        if list1[i] in dict1:
            return [dict1[list1[i]],i]
        else:
            dict1[target-list1[i]] = i
print(two_numbers())