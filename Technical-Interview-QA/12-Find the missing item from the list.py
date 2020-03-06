"""
Find the missing item from the list.
Two lists are provided one having full items and other having partial items.
find the missing items from the list.
Example:
full_list = [1,2,3,4,5]
partial_list = [1,2,3,5]
missing item = 4
"""

full_list = [1, 2, 3, 4, 5, 10, 12]
partial_list = [1, 2, 3, 5]

def missing_item(full_list, partial_list):
    missing_items = []
    for i in full_list:
        if i not in partial_list:
            missing_items.append(i)
    print(missing_items)

missing_item(full_list, partial_list)
