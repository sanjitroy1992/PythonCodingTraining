"""
Q. Given two strings, check if two strings are anagram of each other or not.

Now, before we go about it.. let's understand the problem statement clearly.
Let's consider the below examples.
1.
# sring1 = 'practice makes perfect'
# sting2 = 'perfect makes practice'
here both stings are anagram of each other!
2.
# string1 = 'allergy'
# string2 = 'allergic'
here both strings are not anagram of each other!

Steps:
1. Remove all the spaces form both the strings.
2. If length of both the strings are not same return False.
3. create a dictionary for every sting and map all the key to value 0.
4. now, in for loop for every character if the ch is present in both the dictionary increment the key value by 1.
5. At the end if both the dictionary are equal to each other then it's an anagram else not.

Youtube:https://youtu.be/iUK0cKV_lT4?list=PL5tcWHG-UPH1D-JVSiZI_8I8LPUJtoHdg
"""

def is_anagram():
    string1 = str(input("Enter first string: ")).replace(" ", "").lower()
    string2 = str(input("Enter second string: ")).replace(" ", "").lower()
    if len(string1) != len(string2):
        raise AssertionError("Not Anagram. String lengths are not same!!")

    dict1 = dict.fromkeys(list(string1), 0)
    dict2 = dict.fromkeys(list(string2), 0)
    for i in range(len(string1)):
        dict1[string1[i]] += 1
        dict2[string2[i]] += 1
    if dict1 == dict2:
        print("Anagram!!")
    else:
        print("Not an Anagram!!")
is_anagram()