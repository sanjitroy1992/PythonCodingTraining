"""
Check if a string is Isogram or not
Given a word or phrase, check if it is isogram or not. An Isogram is a word in which no letter occurs more than once.

Examples:

Input : Machine
Output : True
"Machine" does not have any character repeating,
it is an Isogram

Input : Geek
Output : False
"Geek" has 'e' as repeating character,
it is not an Isogram
"""

# Python program to check
# if a word is isogram or not
def is_isogram(word):
    word1= word.lower()
    letter_list=[]
    for letter in word1:
        if(letter.isalpha()):
            if letter in letter_list:
                return False
            else:
                letter_list.append(letter)
    return True

def check_isogram(str1):
    str1=str1.lower()
    n=len(str1)
    count=[0]*26
    for i  in range(n):
        count[ord(str1[i])-ord('a')]+=1
        if(count[ord(str1[i])-ord('a')]>1):
            return False
    return True


if __name__ == '__main__':
    print(is_isogram("Machine"))
    print(is_isogram("isogram"))
    print(is_isogram("GeeksforGeeks"))
    print(is_isogram("Alphabet "))

    print("************************************")
    string = "geeks";
    string2 = "computer";

    # checking str as isogram
    if (check_isogram(string)):
        print("True");
    else:
        print("False");

        # checking str2 as isogram
    if (check_isogram(string2)):
        print("True")

    else:
        print("False");