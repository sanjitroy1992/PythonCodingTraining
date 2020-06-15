"""
Input = "abcabd"
Output = "c"

Input = "abcabdcd"
Output = false

Steps:
- run a for loop and create a dictionary of character and number of times it's repeating
- here non repeating character meaning the character should be only present once in the dictionary.
- run a for loop again and check each character occurrence in the dictionary.
-  if the character if having repeating only once the we have found the character and return the character.
-  if not found return false
"""
def non_repeating(string):
    dict1 = {}
    for i in range(len(string)):
        if string[i] in dict1:
            dict1[string[i]] += 1
        else:
            dict1[string[i]] = 1
    for i in range(len(string)):
        if string[i] in dict1:
            if dict1[string[i]] == 1:
                return string[i]
    return False


print(non_repeating("abcabd"))