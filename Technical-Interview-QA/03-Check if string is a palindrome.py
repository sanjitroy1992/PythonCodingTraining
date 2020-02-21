"""
Q. Given a string write a function to determine if it is a palindrome.

Now, before we go about it.. let's understand the problem statement clearly.
Let's consider the below examples.
1.
# racecar --> Palindrome
# madam --> Palindrome
# Dammit I'm mad --> Palindrome (Provided we are removing all the spaces and punctuations)
# python -- Not a Palindrome

Steps:
1. Remove all the spaces of the string.
2. Use sting module to remove all the punctuation with None.
3. convert sting to lowarcase.
4. check if string and reversed sting has the same characters.

Youtube:https://youtu.be/y3S0iYFedCw?list=PL5tcWHG-UPH1D-JVSiZI_8I8LPUJtoHdg
"""
import string

## Solution 1:

def is_palindrome1():
    s = str(input("Enter first string: "))
    s = s.lower()
    s = s.translate(str.maketrans('', '', string.punctuation))
    s = s.replace(" ", "")
    if s == s[::-1]:
        print("Palindrome!!")
    else:
        print("Not a Palindrome!!")

## Solution 2:
### It is a interesting question . But many times interviewer want from an applier to write an exactly algorithm which perform a comparison .

####In this case we can provide something like :

def is_palindrome2():
    s = str(input("Enter first string: "))
    s = s.translate(str.maketrans('', '', string.punctuation)).lower().replace(" ", "")
    print(s)

    for x, y in zip(range(int(len(s) / 2)), range(int(len(s) - 1), int(len(s) / 2), -1)):
        try:
            if s[x] != s[y]:
                print('Not a Palindrome!')
                break
        except:
            print("Palindrome!!")

# is_palindrome1()
# is_palindrome2()