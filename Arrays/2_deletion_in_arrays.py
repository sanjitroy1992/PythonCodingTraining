"""
Deletion in a 1D array

for(i = idx+1; i < len; i++)
{
    arr[i-1] = arr[i];
}

len = len-1;

Time Complexity in worst case of this insertion operation can be linear i.e. O(N) as we might have to shift all of the elements by one place to the left.


"""

l=[0,1,2,3,4,5,6,7,8,9]
pos=6
index=pos-1
for i in range(index,len(l)-1):
    # print(l)
    swap = l[i]
    l[i] = l[i+1]
    l[i+1] = swap

print(l)
l.pop()
print(l)

