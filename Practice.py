"""
1:Move all zeros present in array to the end.
ex: a = [6,0,8,2,3,0,4,0,1]
o/p: [6,8,2,3,4,1,0,0,0]
"""
a = [6,0,8,2,3,0,4,0,1]
def move_zeros(a):
    n = len(a)
    count = 0
    for i in range(n):
        if a[i] != 0:
            a[count] = a[i]
            count += 1
    while(count<n):
        a[count] = 0
        count += 1
    return a

"""
Problem: 2
Input: "Save water save earth"
Output:
S 1 Times
a 4 Times
v 2 Times
e 4 Times
w 1 Times
t 2 Times
r 2 Times
s 1 Times
h 1 Times
"""
# Input = "Save water save earth@"
# # Input = "Hello World!"
# def print_occurence(Input):
#     if len(Input) == 0:
#         raise AssertionError("Input value does not have any characters")
#     dict1 = {}
#     Input = Input.replace(" ","")
#     for i in range(len(Input)):
#         if Input[i].isalpha():
#             if Input[i] in dict1:
#                 dict1[Input[i]] += 1
#             else:
#                 dict1[Input[i]] = 1
#     for key, value in dict1.items():
#         print("{} {} Times".format(key, value))

# print(print_occurence(Input))

# string = "GeeksforGeeksforGeeksforGeeks"
# substring = "Geeks"
# n = len(string)
# m = len(substring)
# counter = 0
# for i in range(n-m+1):
#     flag = 0
#     for j in range(m):
#         if substring[j] != string[i+j]:
#             flag = 1
#             break
#     if flag == 0:
#         counter += 1
#         print('pattern found at index: {}'.format(i))

# def search(txt,pat):
#     n=len(txt)
#     m=len(pat)
#     for i in range(n-m+1):
#         flag = 0
#         for j in range(m):
#             if(txt[i+j]!=pat[j]):
#                 flag=1
#                 break
#         if(flag==0):
#             print("patter {} found at {}".format(pat,i))
#
# search(string, substring)
# x = list(map(str, input().strip().split(" ")))
# print(x)
# print(max(x))
# def hello():
#     s1 = "SanjitSan"
#     s2 = "Sa"
#     return -1
# print(hello())
