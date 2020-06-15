"""
Time complexity:
O(nlogn) -> Best,  Average Case and Worst Case
O(n) -> Space

Steps:
Create a function for merge two sorted list function call it merge
Create a function to write merge sort by passing one list
"""
def merge(A,B):
    merge_list = []
    i = 0
    j = 0
    if not A:
        return B
    if not B:
        return A
    while (i <= len(A) - 1 and j <= len(B) - 1):
        # print(A[i], B[j])
        if A[i] <= B[j]:
            merge_list.append(A[i])
            i += 1
        else:
            merge_list.append(B[j])
            j += 1
    if i == len(A):
        for x in range(j, len(B)):
            merge_list.append(B[x])
    if j == len(B):
        for x in range(i, len(A)):
            merge_list.append(A[x])
    return merge_list

def merge_sort(a):
    if len(a)<=1:
        return a
    mid = len(a)//2
    left, right = merge_sort(a[:mid]), merge_sort(a[mid:])
    return merge(left, right)

l = [10,4,5,6,7,434]
print(l)
print(merge_sort(l))


# a = [1,2,3,4]
# b= [5,6,7]
# print(merge(a,b))