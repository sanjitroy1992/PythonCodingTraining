Input = [2, 3, 3, 4, 5, 6, 6, 7, 8, 8]
Output = [2, 3, 4, 5, 6, 7, 8]

# Input = ['a', 'a', 'b', 'c', 'd', 'd', 'e', 'f', 'g', 'g']
# Output = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

List1 = []
for i in range(len(Input)):
    if Input[i] not in List1:
        List1.append(Input[i])
print(List1)
List1 = []
[List1.append(i) for i in Input if Input[i] not in List1]
print(List1)
#
#
#
# list = []
# for i in range(len(Input)):
#     if Input[i] not in list:
#         list.append(Input[i])
# print(list)
# list1 = []
# [list1.append(Input[i]) for i in range(len(Input)) if Input[i] not in list1]
# print(list1)


# number = input().split(" ")
# list1 = []
# for i in number:
#     list1.append(int(i))
# print(list1)

# num = list(map(int, input("\nEnter the numbers : ").strip().split(" ")))
# print("Original list: {}".format(num))
# for index, item in enumerate(num):
#     if item == 3:
#         num[index] = 6
# num = [6 if i == 3 else i for i in num]
# print(num)
# list1 = []
# [list1.append(i) for i in num if i not in list1]
# print(list1)