"""
run a for loop to push the items into the stack and then pop one by one item and add to rev string.
Time Complexity: Linear time - O(n)
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


def reverse(stack, input_string=None):
    for i in range(len(input_string)):
        stack.push(input_string[i])
    rev = ''
    while not stack.is_empty():
        rev += stack.pop()
    return rev


s = Stack()
print(reverse(s, "Hello"))
