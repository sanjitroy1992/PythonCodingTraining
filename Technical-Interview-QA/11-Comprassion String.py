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
1. .
2. If the length of the row is one then return median from that matrix.
3. else for every row add all in the matrix add the list of values to a new list
4. sort the new list using 'sorted' inbuilt function
5. return the median = newlist[len(newlist)//2]

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