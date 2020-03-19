"""
Given a list of numbers, write a Python program to print all positive numbers in given list.

Example:

Input: list1 = [12, -7, 5, 64, -14]
Output: 12, 5, 64

Input: list2 = [12, 14, -95, 3]
Output: [12, 14, 3]
"""
list1 = [12, -7, 5, 64, -14]
##Sol: 1

# for i in list1:
#     if i >= 0:
#         print(i, end=" ")

##Sol: 2
list2 = [num for num in list1 if num >= 0]
print(list2)