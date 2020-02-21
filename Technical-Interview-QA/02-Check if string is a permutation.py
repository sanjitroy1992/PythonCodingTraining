"""
Q. Given two strings write a function to decide if one is a permutation of the other.

Now, before we go about it.. let's understand the problem statement clearly.
Let's consider the below examples.
1.
# Driving (Baseline string)
# Drivign (here all the characters are same as the baseline sting and also the last two chracters are swapped) --> Permutation
# riving (here the starting character 'D' is missing. hence the lenght of this sting is smaller that the baseline string) -->Not Permutation
# Criving (here the starting character 'D' is missing even though the length is same compare to the baseline string) -->Not Permutation

2.
"The cow jumps over the moon" -->(Baseline)
"The cow jumps over     the moon" -->(here we have more space in between compared to the baseline string)

The idea is that we need to understand in second example to make both the sting permutable we need to make sure the length of the sting is same.
hence replace all spaces with no space.

Steps:
1. Remove all the spaces form both the strings.
2. If length of both the strings are not same return False.
3. check character of 1st string is present in 2nd string. if yes! then using for loop for every itrator remove the character from 2nd string by replacing ch with "" (space).

Youtube:https://youtu.be/71UjBGz-o0w?list=PL5tcWHG-UPH1D-JVSiZI_8I8LPUJtoHdg
"""

def is_permutation():
    sting1 = str(input("Enter first string: ")).replace(" ", "")
    sting2 = str(input("Enter second string: ")).replace(" ", "")
    if len(sting1) != len(sting2):
        raise AssertionError("Not Permutation. String lengths are not same!!")
    for ch in sting1:
        if ch in sting2:
            sting2 = sting2.replace(ch, "")
    if len(sting2) == 0:
        print("Permutation!!")
    else:
        print("Not Permutation!!")
is_permutation()