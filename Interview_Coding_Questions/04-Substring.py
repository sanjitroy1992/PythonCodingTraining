"""
Write a program to find the substring in a string.
String = "ABABACADAB"
Substring = "AB"
Output: [0,2,7] --> Index value of the staring of the Substring
"""
def substring(string, substr):
    n = len(string)
    m = len(substr)
    index = []
    print(n-m)
    for i in range(n-m+1):
        flag = 0
        for j in range(m):
            if string[i+j] != substr[j]:
                flag = 1
                break
        if flag == 0:
            index.append(i)
    if len(index):
        print("Substring found in index value: {}".format(index))
    else:
        print("Substring not found!")

string = "ABAABACADAB"
substr = "AB"
substring(string, substr)