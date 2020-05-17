"""
Find the two numbers whose addition is the target value in the list.
"""
numbers = [1, 2, 5, 15, 10]
target = 20

def sub_problem():
    if len(numbers) < 2:
        return False
    flag = 0
    for i in range(len(numbers)):
        for j in range((i+1), len(numbers)):
            if (numbers[i] + numbers[j]) == target:
                flag = 1
                return numbers[i], numbers[j]
    if flag == 0:
        return False

print(sub_problem())




def sum_prob():
    num = [1, 3, 11, 2, 7]
    target = 9
    dict1 = {}
    for i in range(len(num)):
        if num[i] in dict1:
            return dict1[num[i]], i
        else:
            dict1[target-num[i]] = i
    print(dict1)
print(sum_prob())
