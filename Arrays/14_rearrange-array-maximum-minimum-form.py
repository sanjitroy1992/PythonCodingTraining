"""

Rearrange an array in maximum minimum form | Set 1
Given a sorted array of positive integers, rearrange the array alternately i.e first element should be maximum value, second minimum value, third second max, fourth second min and so on.

Examples:

Input: arr[] = {1, 2, 3, 4, 5, 6, 7}
Output: arr[] = {7, 1, 6, 2, 5, 3, 4}

"""

arr=[1, 2, 3, 4, 5, 6, 7]

n=len(arr)
temp=[None]*n
s,l=0,n-1
k=0
for i in range(n):
    if (k%2==0):
        temp[i]=arr[l]
        l-=1
    else:
        temp[i]=arr[s]
        s+=1
    k+=1

print(temp)