"""
Find the two numbers whose addition is the target value in the list. Make sure the list is in sorted order.
"""
num = [1, 2, 5, 10, 15]
target = 20

# num = [-2, 1, 2, 4, 7, 11]
# target = 13

"""
Method 1 uses two for loop to loop through the elements in the num list and try to find the target value.
Time complexity: O(n) and Space: O(n) because we have used  dict to store the values.
"""

def sum_prob_linear_time(num, target):
    dict1 = {}
    for i in range(len(num)):
        if num[i] in dict1:
            return dict1[num[i]], i
        else:
            dict1[target-num[i]] = i
    return False
print(sum_prob_linear_time(num, target))

"""
Method 2 uses two for loop to loop through the elements in the num list and try to find the target value.
Time complexity: O(n**2) and Space: O(1) because we didn't use any dict to store the values.
"""
def sum_prob_first_method(num, target):
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if num[i] + num[j] == target:
                return num[i], num[j]
    return False

print(sum_prob_first_method(num, target))

"""
Method 2 uses two for loop to loop through the elements in the num list and try to find the target value.
Time complexity: O(n) and Space: O(n) because we have used  dict to store the values.
"""

def sum_prob_linear_time(num, target):
    dict1 = {}
    for i in range(len(num)):
        if num[i] in dict1:
            return dict1[num[i]], i
        else:
            dict1[target-num[i]] = i
    return False
print(sum_prob_linear_time(num, target))

"""
Method 3 uses two for loop to loop through the elements in the num list and try to find the target value.
Time complexity: O(n) and Space: O(n) because we have used  dict to store the values.
"""
def sum_prob(num, target):
    i = 0
    j = len(num)-1
    while(i<=j):
        if num[i] + num[j] == target:
            return num[i], num[j]
        elif num[i] + num[j] < target:
            i += 1
        else:
            j -= 1
    return False


print(sum_prob(num, target))

