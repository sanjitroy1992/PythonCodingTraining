"""
Stack Data Structure
Suppose you have the following books: A B C D
now if you stack them they would look like,
D
C
B
A
If you would retrieve the books from the stack the order would be D, C, B, A.
You would do it from the top book towards bottom.
Tow thing we need to remember here.
one: In order to keep a book we need to push it into the stack.
Two: In order to retrieve a book we need to pop it from the stack.
Hence Push and Pop are two fundamental routine that we need fot stack data structure.

Below we have created a class called Stack.
Methods:
    init: initializes an empty list.
    push: to push an item into the stack.
    pop: retrieve an item from the stack.
    is_empty: to check if the stack is empty.
    peek: checks if the stack is not empty then returns the last item from the stack.
    get_stack: return the current elements from the stack.

Youtube: https://youtu.be/lVFnq4zbs-g?list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items


# s = Stack()
# s.push('A')
# s.push('B')
# print(s.get_stack())
# print(s.pop())
# print(s.get_stack())
# print(s.is_empty())
# print(s.peek())
# print(s.pop())
# print(s.is_empty())