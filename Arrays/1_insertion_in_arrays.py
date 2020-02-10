"""
Insertion in a 1D array

Now, before inserting the element at the index idx, shift all elements from the index idx till end of the array to the right by 1 place. This can be done as:
for(i = len-1; i >= idx; i--)
{
    arr[i+1] = arr[i];
}
After shifting the elements, place the element K at index idx.
arr[idx] = K;

Time Complexity in worst case of this insertion operation can be linear i.e. O(N) as we might have to shift all of the elements by one place to the right.

"""

l=[0,1,2,3,4,5,6,7,8,9]
l.append(None)
# print(l)
pos=7
index=pos-1
item_to_insert = "abc"
for i in range(len(l)-2,index-1,-1):
    l[i+1]=l[i]
l[index]= item_to_insert
print(l)
