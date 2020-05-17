data = [1, 3, 5, 6, 7, 8, 9, 12, 15, 18, 22, 25, 30]
target = 15
"""
Binary Search: This allows to search for a target element in a sorted list.
Here we'll see both the Iterative and Recursive method to implement a Binary Search Tree!
In case linear search the time complexity is of O(n). So for in case of a billion data it will take billion times of iteration
youtube: https://youtu.be/zeULw-a7Mw8?list=PL5tcWHG-UPH1K7oTJgIbWy6rCMc8-8Lfm

Space Complexity: O(1)
Time Complexity: O(logN)

"""
## 1. Linear search:
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False
# print(linear_search(data, target))

## 2. Itrative Binary Search
def iterative_binary_search(data, target):
    low = 0
    high = len(data)-1
    while low <= high:
        mid = int((low + high)/2)
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

# print(iterative_binary_search(data, target))

##Recursive Binary Search:
def recursive_binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = int((low + high)/2)
        if target == data[mid]:
            print("True")
        elif target < data[mid]:
            recursive_binary_search(data, target, low, mid - 1)
        else:
            recursive_binary_search(data, target, mid + 1, high)

# print(recursive_binary_search(data, target, 0, len(data)-1))


def bsearch():
    list1 = [2,3,4,5,6,7,8]
    target = 7
    low = 0
    high = len(list1)
    flag = 0
    while(low<=high):
        mid = (low+high)//2
        if mid == target:
            flag = 1
            return True
        elif(target>mid):
            low = mid+1
        else:
            high = mid-1
    if flag == 0:
        return False
# print(bsearch())

class stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def get_stack(self):
        return self.items

s = stack()
s.push("A")
s.push("B")
s.push("C")
s.push("D")
print(s.get_stack())
print(s.peek())
s.pop()
print(s.get_stack())