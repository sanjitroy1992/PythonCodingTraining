"""
Selection sort finds the lowest element in the list and keeps pushing it to the from of the list
Best and Avg time complexity: O(nlogn)
Worst case: O(n*2)
"""
unsorted_list = [3, 5, 1, 7, 2, 9]
def selection_sort(unsorted_list):
    for i in range(len(unsorted_list)):
        smallest_index = i
        for j in range(i+1, len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[smallest_index]:  #checking if current value is smaller or greater than the smallest index
                smallest_index = j  #setting the smallest value to the variable
        unsorted_list[smallest_index], unsorted_list[i] = unsorted_list[i], unsorted_list[smallest_index] #swapping smallest and current value
    return unsorted_list

print(selection_sort(unsorted_list))
