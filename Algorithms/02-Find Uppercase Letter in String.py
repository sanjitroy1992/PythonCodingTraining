String1 = "Hello World"
String2 = "helloworLd"
String3 = "helloworld"
"""
Youtube:https://youtu.be/dlCGc92tAqo?list=PL5tcWHG-UPH1K7oTJgIbWy6rCMc8-8Lfm
"""
## 1. Find Uppercase Iterative
def find_uppercase_iterative():
    string = str(input("Enter the string: ")).replace(" ","")
    for i in range(len(string)):
        if string[i].isupper():
            return string[i]
    return False
print(find_uppercase_iterative())

## 2. Find Uppercase Recursive
def find_uppercase_recursive(string, idx=0):
    if str(string[idx]).isupper():
        return string[idx]
    elif idx == len(string)-1:
        return "No uppercase letter found"
    return find_uppercase_recursive(string, idx+1)

# print(find_uppercase_recursive(String1))