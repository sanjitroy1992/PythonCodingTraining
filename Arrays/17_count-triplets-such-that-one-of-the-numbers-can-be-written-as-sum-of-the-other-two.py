"""
Count Triplets such that one of the numbers can be written as sum of the other two
Given an array A[] of N integers. The task is to find the number of triples (i, j, k) , where i, j, k are indices and (1 <= i < j < k <= N), such that in the set { A_i, A_j, A_k} at least one of the numbers can be written as the sum of the other two.

Examples:

Input : A[] = {1, 2, 3, 4, 5}
Output : 4
The valid triplets are:
(1, 2, 3), (1, 3, 4), (1, 4, 5), (2, 3, 5)

Input : A[] = {1, 1, 1, 2, 2}
Output : 6


"""

l1=[1,1,1,2,2]
count=0
for i in range(0,len(l1)-2):
    for j in range(i+1,len(l1)-1):
        for k in range(j+1,len(l1)):
            if (l1[k]==l1[i]+l1[j]) or (l1[j]==l1[i]+l1[k]) or (l1[i]==l1[j]+l1[k]):
                print("{} {} {}".format(l1[i],l1[j],l1[k]))
                count += 1
print(count)

