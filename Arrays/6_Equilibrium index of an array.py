"""

Description - Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes. We are given an Array of integers, We have to find out the first index i from left such that -
A[0] + A[1] + ... A[i-1] = A[i+1] + A[i+2] ... A[n-1]
Input
[-7, 1, 5, 2, -4, 3, 0]
Output
3
A[0] + A[1] + A[2] = A[4] + A[5] + A[6]
Naive Solution : We can iterate for each index i and calculate the leftsum and rightsum and check whether they are equal.
for (i=0 to n-1)
{
    leftsum = 0
    for (j = 0 to i-1)
        leftsum += arr[i]
    rightsum = 0
    for (j = i+1 to n-1)
        rightsum += arr[i]

    if leftsum == rightsum :
        return i
}
Time Complexity : O(n^2)
Auxiliary Space : O(1)

"""



