"""

Given a binary string, count number of substrings that start and end with 1.
Given a binary string, count number of substrings that start and end with 1. For example,
if the input string is “00100101”, then there are three substrings “1001”, “100101” and “101”.
Source: Amazon Interview Experience | Set 162

A Simple Solution is to run two loops. Outer loops picks every 1 as starting point and inner loop searches for ending 1
and increments count whenever it finds 1.
"""

str1 = "00100101"
n=len(str1)
count=0
for i in range(n):
    if str1[i]=='1':
        for j in range(i+1,n):
            if(str1[j]=='1'):
                count+=1
print(count)
