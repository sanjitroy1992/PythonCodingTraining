Input = [2, 3, 3, 4, 5, 6, 6, 7, 8, 8]
Output = [2, 3, 4, 5, 6, 7, 8]

# Input = ['a', 'a', 'b', 'c', 'd', 'd', 'e', 'f', 'g', 'g']
# Output = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

List1 = []
for i in range(len(Input)):
    if Input[i] not in List1:
        List1.append(Input[i])
print(List1)
# List1 = []
# [List1.append(i) for i in Input if Input[i] not in List1]
# print(List1)
#
#
