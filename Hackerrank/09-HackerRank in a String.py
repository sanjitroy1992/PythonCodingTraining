"""

"""
l1 = ['h', 'a', 'c', 'k', 'e', 'r', 'r', 'a',' n', 'k']
q = int(input())
for q_itr in range(q):
    s = list(map(str,input()))
    print(l1)
    print(s)
    for i in range(len(l1)):
        print(i)
        print(l1[i])
        if l1[i] in s:
            l1.remove(l1[i])
            s.remove(l1[i])
            print(l1)
            print(s)
    if len(l1) == 0:
        print('YES')
    else:
        print('NO')
