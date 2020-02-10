"""
Pangram Checking
Given a string check if it is Pangram or not. A pangram is a sentence containing every letter in the English Alphabet.

Examples : The quick brown fox jumps over the lazy dog ” is a Pangram [Contains all the characters from ‘a’ to ‘z’]
“The quick brown fox jumps over the dog” is not a Pangram [Doesn’t contains all the characters from ‘a’ to ‘z’, as ‘l’, ‘z’, ‘y’ are missing]

We create a mark[] array of Boolean type. We iterate through all the characters of our string and whenever we see a character we mark it. Lowercase and Uppercase are considered the same. So ‘A’ and ‘a’ are marked in index 0 and similarly ‘Z’ and ‘z’ are marked in index 25.

"""

str1="The quick brown fox jumps over the lazy do"
flag=1
mark= [False]*26

for i, letter in enumerate(str1):
    if(ord('a')<=ord(letter)<=ord('z')):
        index= ord(letter) - ord('a')
    elif(ord('A')<=ord(letter)<=ord('Z')):
        index = ord(letter) - ord('A')
    mark[index]=True

for i in range(26):
    if(mark[i]==False):
        print("{} is not pangram".format(str1))
        flag=0
        break

if(flag==1):
    print("{} is pangram".format(str1))

