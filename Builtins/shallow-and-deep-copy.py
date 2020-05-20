import copy
old_list = [[1,2,3], [4,5,6], [7,8,9]]
new_list = old_list

print("New variable assignment - Both new and old id are same")
print("old list: {} and id {}".format(old_list, id(old_list)))
print("new list: {} and id {}".format(new_list, id(new_list)))

print("\n***Shallow Copy***\nA shallow copy creates a new object which stores the reference of the original elements.")
new_list_shallow_copy = copy.copy(old_list)
print("\nShallow Copy - Both new and old id are different")

print("old list: {} and id {}".format(old_list, id(old_list)))
print("new list: {} and id {}".format(new_list_shallow_copy, id(new_list_shallow_copy)))
print("\nIn the above program, we created a shallow copy of old_list. The new_list contains references to original "
      "nested objects stored in old_list. \nThen we add the new list i.e [4, 4, 4] into old_list."
      "This new sublist was not copied in new_list."
      "\nHowever, when you change any nested objects in old_list, the changes appear in new_list.")

old_list[1][1] = 'AA'
print("\nIn the above program, we made changes to old_list i.e old_list[1][1] = 'AA'. Both sublists of old_list "
      "\nand new_list_shallow_copy at index [1][1] were modified. This is because, both lists share the reference of same nested objects.")
print("old list: {}".format(old_list))
print("new list: {}".format(new_list_shallow_copy))
print("\nAdded [4, 4, 4] to the old_list. Notice it's only reflecting in the new variable")
old_list.append([4,4,4])
print("old list: {}".format(old_list))
print("new list: {}".format(new_list_shallow_copy))


print("\n***Deep Copy***\nA deep copy creates a new object and recursively adds the copies of nested objects present in the original elements.")
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list_deep_copy = copy.deepcopy(old_list)
print("\nDeep Copy - Both new and old id are different")
print("old list: {} and id {}".format(old_list, id(old_list)))
print("new list: {} and id {}".format(new_list_deep_copy, id(new_list_deep_copy)))

print("In the above program, we use deepcopy() function to create copy which looks similar."
      "\nHowever, if you make changes to any nested objects in original object old_list, you’ll see no changes to the copy new_list.")

print("\n Update a value in nested list in old list")
old_list[1][0] = 'BB'

print("Old list:", old_list)
print("New list:", new_list_deep_copy)

print("\nIn the above program, when we assign a new value to old_list, we can see only the old_list is modified. "
      "\nThis means, both the old_list and the new_list are independent. This is because the old_list was recursively copied, "
      "\nwhich is true for all its nested objects.")