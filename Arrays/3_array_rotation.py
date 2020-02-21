"""
Rotation in a 1D array by 'k'

Say, arr[] = [1, 2, 3, 4, 5, 6, 7], K = 2
1) Store first K elements in a temp array
   temp[] = [1, 2]
2) Shift rest of the arr[]
   arr[] = [3, 4, 5, 6, 7, 6, 7]
3) Store back the K elements from temp
   arr[] = [3, 4, 5, 6, 7, 1, 2]

"""

l=[0,1,2,3,4,5,6,7,8,9]
temp=[]
k=2
for i in range(0,k):
    temp.append(l[i])
# print(temp)

j=0
for i in range(k,len(l)):
    l[j] = l[i]
    j+=1

# print(l)

j=0
for i in range(len(l)-k,len(l)):
    l[i]=temp[j]
    j+=1
print(l)

