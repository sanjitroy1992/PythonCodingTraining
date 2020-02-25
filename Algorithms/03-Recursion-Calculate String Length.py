"""
Youtube:https://youtu.be/RRK0gd77Ln0?list=PL5tcWHG-UPH1K7oTJgIbWy6rCMc8-8Lfm
"""

def iterative_string_length():
    string = str(input("Enter the string: "))
    count = 0
    for i in range(len(string)):
        count += 1
    return count
# print(iterative_string_length())

def recursive_string_length(string):
    if string == '':
        return 0
    return 1 + recursive_string_length(string[1:])

print(recursive_string_length('hello'))