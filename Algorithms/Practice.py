"""
Binary Search
"""
data = [1,5,7,9,11,14,18,20]
target = 20

def binary_search(data, target):
    low = 0
    high = len(data)-1
    while(low<=high):
        mid = (low+high)//2
        if data[mid] == target:
            return True
        elif(target<data[mid]):
            high = mid - 1
        elif(target>data[mid]):
            low = mid + 1
    return False
# print(binary_search(data, target))

"""
Remove Duplicate items from a list
"""
Input = [2, 3, 3, 4, 5, 6, 6, 7, 8, 8]

list1 = []
for i in range(len(Input)):
    if Input[i] not in list1:
        list1.append(Input[i])
# print(list1)

# [list1.append(Input[i]) for i in range(len(Input)) if Input[i] not in list1]
# print(list1)

"""
Find intersection between two lists
"""
A = [1, 2, 3, 4, 4, 5]
B = [2, 2, 3, 5, 6]
def intersection_list():
    intersection = []
    i = 0
    j = 0
    while(i<len(A) and j<len(B)):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i-1]:
                intersection.append(A[i])
            i += 1
            j += 1
        elif A[i]>B[j]:
            j += 1
        else:
            i += 1
    return intersection

# print(intersection_list())


