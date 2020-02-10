"""
Given a string, find its first non-repeating character
Given a string, find the first non-repeating character in it. For example, if the input string is “GeeksforGeeks”, then output should be ‘f’ and if input string is “GeeksQuiz”, then output should be ‘G’.


We can use string characters as index and build a count array. Following is the algorithm.

1) Scan the string from left to right and construct the count array.
2) Again, scan the string from left to right and check for count of each
 character, if you find an element who's count is 1, return it.

"""

# Python program to print the first non-repeating character
NO_OF_CHARS = 256

def firstRepeating(string):
    count=[0]*NO_OF_CHARS
    for letter in string:
        count[ord(letter)]+=1
        if(count[ord(letter)])>1:
            return letter

def firstNonRepeating(string):
    count = [0] * NO_OF_CHARS
    for letter in string:
        count[ord(letter)] += 1
    for letter in string:
        if (count[ord(letter)]) == 1:
            return letter






# Driver program to test above function
string = "geeksforgeeks"
letter = firstRepeating(string)
print("First repeating character is " + letter)

letter = firstNonRepeating(string)
print("First non-repeating character is " + letter)