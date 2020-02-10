"""
Leaders in an array
Write a program to print all the LEADERS in the array. An element is leader if it is greater than all the elements to its right side. And the rightmost element is always a leader. For example int the array {16, 17, 4, 3, 5, 2}, leaders are 17, 5 and 2.
Let the input array be arr[] and size of the array be size.


Method 1 (Simple)
Use two loops. The outer loop runs from 0 to size – 1 and one by one picks all elements from left to right. The inner loop compares the picked element to all the elements to its right side. If the picked element is greater than all the elements to its right side, then the picked element is the leader.
"""

arr=[16, 17, 4, 3, 5, 2]
n=len(arr)
for i in range(n):
    for j in range(i+1,n):
        if(arr[i]<=arr[j]):
            break
    if(j==n-1):
        pass
        print(arr[i])

"""
Method 2 (Scan from right)
Scan all the elements from right to left in an array and keep track of maximum till now. When maximum changes its value, print it.
"""

print("*****************************")
arr=[16, 17, 4, 3, 5, 2]
n=len(arr)

max_from_right=arr[-1]
print(max_from_right)
for i in range(n-2,-1,-1):
    if arr[i]>max_from_right:
        max_from_right = arr[i]
        print(max_from_right)


