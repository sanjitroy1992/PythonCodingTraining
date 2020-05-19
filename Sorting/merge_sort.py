"""
Time complexity:
O(nlogn) -> Best,  Average Case and Worst Case
O(n) -> Space
"""


# def merge(a,b):
#     c = []
#     a_idx = 0
#     b_idx = 0
#     print(a, b)
#     while(a_idx<len(a) and b_idx<len(b)):
#         if a[a_idx] < b[b_idx]:
#             c.append(a[a_idx])
#             a_idx += 1
#         else:
#             c.append(b[b_idx])
#             b_idx += 1
#         # print(c)
#         if a_idx == len(a): c.extend(b[b_idx:])
#         else: c.extend(a[a_idx:])
#     return c
#
# def merge_sort(a):
#     if len(a)<=1:
#         return a
#     mid = len(a)//2
#     left, right = merge_sort(a[:mid]), merge_sort(a[mid:])
#     print(left, right)
#     return merge(left, right)
#
# # l = [10,4,5,6,7,434]
# # print(l)
# # print(merge_sort(l))
# a = [1,2,3,4]
# b= [5,6,7]
# print(merge(a,b))

# Python program for implementation of
# MergeSort (Alternative)


def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # The value from the left half has been used
                myList[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1


myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(myList)
print(myList)