"""
Q. Write a function to replace all the spaces in a sting with '%20'.

Example:
    string = 'Mr. Steve Smith'
    output = 'Mr.%20Steve%20Smith'

Youtube:https://youtu.be/rxgVVwZlJko
"""

def URLify():
    string = str(input("enter the string having spaces: "))
    output_string = ''
    for i in range(len(string)):
        if string[i] == " ":
            output_string += '%20'
        else:
            output_string += string[i]
    return output_string

print(URLify())