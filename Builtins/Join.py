list1 = ["This", "is", "the", "best", "time"]

## join the list items using for loop:
for i in list1:
    print(i, end=" ")

## join the list items using join function
print("".join(list1))
print(" ".join(list1).upper())
print(", ".join(list1))

reversestring = lambda x: "".join(reversed(x))
lis1 = list(map(reversestring, list1))
print(", ".join(lis1))

list1 = [2,4,5,9]
# a = lambda x: x%2 == 0
# list2 = list(map(a, list1))
# print(list2)
# for i in range(len(list2)):
#     print(list2[i])