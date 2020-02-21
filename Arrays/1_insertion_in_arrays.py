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

# l=[0,1,2,3,4,5,6,7,8,9]
# l.append(None)
# # print(l)
# pos=7
# index=pos-1
# item_to_insert = "abc"
# for i in range(len(l)-2,index-1,-1):
#     l[i+1]=l[i]
# l[index]= item_to_insert
# print(l)

# arr = [0,1,2,3,4,5,6,7,8,9]
# pos = 2
# element = "abc"
# arr.append(None)
# print(arr)
# index = pos-1
# for i in range(len(arr)-2, index-1, -1):
#     print("old value: {} new value: {}".format(arr[i + 1], arr[i]))
#     arr[i+1] = arr[i]
# print(arr)
# arr[index] = element
# print(arr)
#
# ## rotate an 1D array
# arr = [0,1,2,3,4,5,6,7,8,9]
# pos = 2

# testcases = int(input("number of test cases: "))
# list1 = []
# for t in range(testcases):
#     n, s = str(input("")).split(" ")
#     for i in range(0, int(n)):
#         print("i: {}".format(i))
#         arr = str(input("array")).split(" ")
#         list1.append(arr[i])
# print(n,s)
# print(list1)

T = int(input())
l1 = []
for _ in range(T):
    N, S = map(int, input().split())
    l = list(map(int, input().split()))
    f = 0
    for i in range(N):
        sum = l[i]
        for j in range(i+1,N):
            sum+=l[j]
            if(sum==S):
                f=1
                break
        if(f==1):
            # print("")
            l1.append((i+1,j+1))
            # print("start:{} end:{}".format(i + 1, j + 1))
            break
print(l1)

for item in l1:
    print("start:{} end:{}".format(item[0],item[1]))
