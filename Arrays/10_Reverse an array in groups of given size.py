arr = [1, 2, 3, 4, 5, 6, 7, 8]
k = 10

for i in range(0,len(arr),k):
    left =i
    right = min(i+k-1,len(arr)-1)
    while(left<right):
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
print(arr)