"""
Q. Given an array of integers, every element appears twice except for one. Find that single one.
Note: Your algorithm should have a linear complexity. Could you implement it without using extra memory?

Now, before we go about it.. let's understand the problem statement clearly.
Let's consider the below examples.
Example:
    num = [1,2,2,3,1]
    output = 3
Solution:
for every item in list check the occurences and add it in the dictionary --> {element:occurrences}
i = 0 --> {1:1}
i = 1 --> {1:1, 2:1}
i = 2 --> {1:1, 2:2}
i = 3 --> {1:1, 2:2, 3:1}
i = 4 --> {1:2, 2:2, 3:1}
now check which value has an occurrence of 1 and return that as an output.

Solution2:
XOR : b1 | b2
      0    0 : 0
      1    0 : 1
      0    1 : 1
      1    1 : 0

# it's 0 ^ 1 = 1, 1 ^ 2 = 3, 3 ^ 2 = 1, 1 ^ 3 = 2, and lastly 2 ^ 1 = 3
Youtube:https://youtu.be/r0CAz6MdgEg?list=PL5tcWHG-UPH1D-JVSiZI_8I8LPUJtoHdg
"""

def single_number():
    num = list(map(int, input("enter the list items: ").strip().split()))
    if len(num) <= 1:
        raise AssertionError("List should have at least two values")
    aux_dic = {}
    for i in range(len(num)):
        if num[i] in aux_dic:
            aux_dic[num[i]] += 1
        else:
            aux_dic[num[i]] = 1
    print(aux_dic)
    try:
        for i, j in aux_dic.items():
            if j == 1:
                return i
    except:
        raise AssertionError("single value is not present")

print(single_number())

## Solution 2


def single_number2():
    num = list(map(int, input("enter the list items: ").strip().split()))
    ans = 0
    for i in num:
        ans ^= i
    print(ans)
# single_number2()