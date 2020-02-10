"""

A Program to check if strings are rotations of each other or not
Given a string s1 and a string s2, write a snippet to say whether s2 is a rotation of s1?
(eg given s1 = ABCD and s2 = CDAB, return true, given s1 = ABCD, and s2 = ACBD , return false)


Algorithm: areRotations(str1, str2)

    1. Create a temp string and store concatenation of str1 to
       str1 in temp.
                          temp = str1.str1
    2. If str2 is a substring of temp then str1 and str2 are
       rotations of each other.

    Example:
                     str1 = "ABACD"
                     str2 = "CDABA"

     temp = str1.str1 = "ABACDABACD"
     Since str2 is a substring of temp, str1 and str2 are
     rotations of each other.

"""

# Python program to check if strings are rotations of
# each other or not

# Function checks if passed strings (str1 and str2)
# are rotations of each other

def areRotations(str1, str2):
    n1=len(str1)
    n2=len(str2)
    if n1!=n2:
        return False
    if(str1+str2).count(str2)>0:
        return True
    else:
        return False

string1 = "AACD"
string2 = "ACDA"

if areRotations(string1, string2):
    print("Strings are rotations of each other")
else:
    print("Strings are not rotations of each other")
