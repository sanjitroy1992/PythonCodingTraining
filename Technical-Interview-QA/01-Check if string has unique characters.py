"""
Q. Implement an algorithm to determine if a string has all unique characters.

Now, before we go about it.. let's understand the problem statement clearly.
Let's consider two specific string.
# unique (here character u is repeated twice)
# Bear (here all the characters are uniques)

One of many ways is to solve this particular problem with module 'set'

Youtube:https://youtu.be/UqEU-obRUnI?list=PL5tcWHG-UPH1D-JVSiZI_8I8LPUJtoHdg
"""

def is_unique():
    sting = input("Enter the sting to check if it's has unique characters: ")
    characters = set(sting)
    if len(sting) == len(characters):
        print("string: {} is unique".format(sting))
    else:
        print("string: {} is not unique".format(sting))