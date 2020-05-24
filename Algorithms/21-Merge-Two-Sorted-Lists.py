def merge_list():
    A = [1,3,5,7,9,10,10,12]
    B = [2,4,6,8,10,11]
    merge_list = []
    i = 0
    j = 0
    if not A:
        return B
    if not B:
        return A
    while(i <= len(A)-1 and j <= len(B)-1):
        # print(A[i], B[j])
        if A[i] <= B[j]:
            merge_list.append(A[i])
            i += 1
        else:
            merge_list.append(B[j])
            j += 1
    if i == len(A):
        for x in range(j, len(B)):
            merge_list.append(B[x])
    if j == len(B):
        for x in range(i, len(A)):
            merge_list.append(A[x])
    return merge_list

print(merge_list())