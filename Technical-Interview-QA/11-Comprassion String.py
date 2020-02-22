"""
Q. String Compression: Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string "aabcccccaaa" would become a2b1c5a3. If the "compressed" string would not become smaller
than the original string, your method should return the original string.
You can assume the string has only uppercase and lowercase letters (a-z).

Now, before we go about it.. let's understand the problem statement clearly.
Let's consider the below examples.

string1 = aabcccccaaa
output = a2b1c5a3

Steps:
1. If the length of the string is less that or equal to 1 the return false.
2. start for loop with the 2nd index till the last index and Compare prev string with the current string and if the are the same then increase the count.
3. else add the string character along with the counter
4. at the end for the last character add the character along with the counter to the compressed string.
5. in the end check if the compressed string length if greater than input string.
6. if yes the return compressed string else return input string.

Youtube: https://youtu.be/sE7F1WroB1M?list=PL5tcWHG-UPH1D-JVSiZI_8I8LPUJtoHdg
"""

def string_comprassion():
    string = str(input("Enter the string to compress: "))
    comp_str = ""
    count = 1
    if len(string) <= 1:
        raise AssertionError("string length must be more that 1")
    for i in range(1, len(string)):
        if string[i-1] == string[i]:
            count += 1
        else:
            comp_str += string[i-1] + str(count)
            count = 1
    comp_str += string[i] + str(count)
    if len(comp_str)>= len(string):
        print(comp_str)
    else:
        print(comp_str)


string_comprassion()