
"""
Frequency of elements in an array
"""

arr=[1,7,1,2,5,7,1,2]
n=len(arr)
visited=[False]*n
# print(visited)
for i in range(n):
    count = 1
    if visited[i]==True:
        continue
    for j in range(i+1,n):
        if arr[i]==arr[j]:
            count+=1
            visited[j]=True
    if(j==n-1):
        print("Frequency of element {} is {}".format(arr[i],count))
