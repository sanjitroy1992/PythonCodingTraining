"""
Given a non-empty array of integers, every element appears twice except one. Find the single one.

Input: [2,2,1]
Output: 1
"""

"""
Method: 1 Using Dict approach
Use array(in Python called list) to store numbers in nums. If some number in nums is new to array, append it.If some 
number is already in the array, remove it

Time complexity : O(n). for i in nums takes O(n) time, and if dict.has_key(i) takes O(1) time.
Space complexity : O(n). We need a hash table of size n to contain elements in nums.
"""
# Approach 1
def single_number(arr):
    dict1 = {}
    for i in range(len(arr)):
        if arr[i] in dict1:
            dict1[arr[i]] += 1
        else:
            dict1[arr[i]] = 1
    for key, value in dict1.items():
        if value == 1:
            return key
print(single_number([2,2,3]))

# Approach 2
def single_number2(arr):
    dict1 = {}
    for i in range(len(arr)):
        if arr[i] in dict1:
            dict1.pop(arr[i])
        else:
            dict1[arr[i]] = 1
    for key, value in dict1.items():
        if value == 1:
            return key

print(single_number2([2,2,1,1,3]))

"""
Method: 2 Using list approach

Use array(in Python called list) to store numbers in nums. If some number in nums is new to array, append it.If some 
number is already in the array, remove it
Time complexity : O(n^2). for i in nums takes O(n) time, and if i in list is also a for-loop taking O(n) time.
Space complexity : O(n). We need a list of size n to contain elements in nums.
"""

def single_number_with_list(arr):
    list1 = []
    for i in arr:
        if i in list1:
            list1.remove(i)
        else:
            list1.append(i)
    if len(list1) != 0:
        return list1.pop()
    else:
        return False

print(single_number_with_list([2,2,1,1,3]))

