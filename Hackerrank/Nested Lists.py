"""
Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the
name(s) of any student(s) having the second lowest grade.

Input:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Output:
Berry
Harry

Solution:
1. Create two lists one having [name , score] and second one having only [scores].
2.
"""
marksheet = []
scores = []
for i in range(int(input())):
    name = input()
    score = float(input())
    marksheet += [[name, score]]
    scores += [score]

TargetScore = float(sorted(set(scores))[1])
length = (len(sorted(marksheet))//2)+1
newmarksheet = sorted(marksheet)
for i in range(length):
    if float(newmarksheet[i][1]) == TargetScore:
        print(newmarksheet[i][0])
