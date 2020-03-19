"""
Given the names and grades for each student in a Physics class of N students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Input Format

The first line contains an integer, N , the number of students.
The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.

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
"""


marksheet = []
scores = []

for _ in range(int(input())):
    name = str(input())
    score = float(input())
    marksheet += [[name, score]]
    scores += [score]

print(marksheet)
TargetScore = sorted(list(set(scores)))[1]
# print(TargetScore)
for i in range(len(marksheet)):
    if marksheet[i][1] == TargetScore:
        print(marksheet[i][0])
