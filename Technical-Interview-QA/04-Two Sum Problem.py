"""
Q. Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Now, before we go about it.. let's understand the problem statement clearly.
Let's consider the below examples.
Example:
    num = [1,3,11,2,7]
    target = 9
    return = [3,4]
Solution:
9-1 = 8 --> {8:0}
9-3 = 6 --> {8:0, 6:1}
9-11 = -2 --> {8:0, 6:1, -2:2}
9-2 = 7 --> {8:0, 6:1, -2:2, 7:3}
now we check if 7 is in the dictionary.
if yes then return.. dict[num[i]], i --> [3,4]
Steps:
1. Check if the num array length is <= 1 else return False.
2. create an empty dictionary.
3. for the i in range(len(num)).
4. if num[i] in dictionary then return dictionary[num[i]], i].
5. else add the difference:index in the dictionary --> dictionary[target-num[i]]=i

Youtube:https://youtu.be/8uYHAM-dtVA?list=PL5tcWHG-UPH1D-JVSiZI_8I8LPUJtoHdg
"""

def two_numbers():
    num = list(map(int, input("enter the list items: ").strip().split()))
    target = int(input("enter the target: "))
    if len(num) <= 1:
        return False
    aux_dic = {}
    for i in range(len(num)):
        if num[i] in aux_dic:
            return [aux_dic[num[i]], i]
        else:
            aux_dic[target-num[i]] = i
print(two_numbers())