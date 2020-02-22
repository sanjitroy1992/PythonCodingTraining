"""
Q. Given a N cross M matrix in which each row is sorted, find the overall median of the martix.
Assume N*M is odd!

Now, before we go about it.. let's understand the problem statement clearly.
Let's consider the below examples.

Matrix=
[1, 3, 5]
[2, 6, 9]
[3, 6, 9]

A = [1, 2, 3, 3, 5, 6, 6, 9, 9]
Median = 5

Steps:
1. We need to consider two types of matrix. one having one row and other having more that one row.
2. If the length of the row is one then return median from that matrix.
3. else for every row add all in the matrix add the list of values to a new list
4. sort the new list using 'sorted' inbuilt function
5. return the median = newlist[len(newlist)//2]

Youtube: https://youtu.be/wn-NKs_KNyQ?list=PL5tcWHG-UPH1D-JVSiZI_8I8LPUJtoHdg
"""

l1 =[1, 3, 5]
l2 = [2, 6, 9]
l3 = [3, 6, 9]
A = [l1, l2, l3]
A1 = [l1]

def matrix_median(A):
    if len(A) == 1:
        median_index = len(A[0])//2
        print(A[0][median_index])
    else:
        new_list = []
        for row in range(len(A)):
            new_list.extend(A[row])
        new_list = sorted(new_list)
        print(new_list[len(new_list)//2])
matrix_median(A)