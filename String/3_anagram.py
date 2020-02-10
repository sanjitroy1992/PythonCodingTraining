"""
Check whether two strings are anagram of each other
Write a function to check whether two given strings are anagram of each other or not. An anagram of a string is another string that contains same characters, only the order of characters can be different. For example, “abcd” and “dabc” are anagram of each other.

Anagram Words

Listen - Silent

Triangle - Integral

Method 1 (Use Sorting)

Sort both strings
Compare the sorted strings

Time Complexity: O(nLogn)

Method 2 (Count characters)
This method assumes that the set of possible characters in both strings is small. In the following implementation, it is assumed that the characters are stored using 8 bit and there can be 256 possible characters.

Create count arrays of size 256 for both strings. Initialize all values in count arrays as 0.
Iterate through every character of both strings and increment the count of character in the corresponding count arrays.
Compare count arrays. If both count arrays are same, then return true.

"""

# Python program to check if two strings are anagrams of
# each other
NO_OF_CHARS = 256

# Function to check whether two strings are anagram of
# each other
def are_anagram(str1, str2):
    count1=[0]*NO_OF_CHARS
    count2 = [0] * NO_OF_CHARS
    for item in str1:
        count1[ord(item)]+=1
    for item in str2:
        count2[ord(item)] += 1
    if (len(str1)!=len(str2)):
        return False
    for i in range(NO_OF_CHARS):
        if(count1[i]!=count2[i]):
            return False
    return True
print(are_anagram("geeksforgeeks", "forgeeksgeeks"))