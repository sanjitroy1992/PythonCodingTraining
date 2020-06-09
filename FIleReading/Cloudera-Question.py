"""
Q1: a text file contains lines of texts as below under content: you need to reverse the words in the line and change
the order of the lines in the output.

/tmp/input.txt
Content:
I love cloudera
I work from home
I work for Ranger


Output:
Ranger for work I
home from work I
cloudera love I
"""
str1 = """I love cloudera
I work from home
I work for Ranger
"""
with open("text.txt", 'r') as f:
    lines = f.readlines()
    list1 = []
    for line in lines:
        list1.append(str(line.strip('\n')).split(" "))
    for i in list1:
        print(" ".join(i[::-1]))
