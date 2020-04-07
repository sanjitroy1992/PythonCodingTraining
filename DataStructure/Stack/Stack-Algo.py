"""
A B C D

D
C
B
A

1. push
2. pop
3. get_stack
4. is_empty
5. peek
"""


class Stack():

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def reverse_string(self, string):
        for i in range(len(string)):
            self.push(string[i])
        rev = ''
        while not self.is_empty():
            s = self.pop()
            rev = rev + s
        return rev


def binary_representtion(integer):
    s = Stack()
    while integer > 0:
        rem = int(integer) % 2
        s.push(rem)
        integer = integer//2
    binary = ''
    for i in range(len(s)):
        binary = str(s[i]) + binary
    print(s.get_stack())
    print(binary)


def is_matched(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    else:
        return False


def balanced_parenthesis(parenthesis):

    """
    ({}) - Balanced
    ({{])) - Not Balanced
    )) - Not Balanced
    """
    s = Stack()
    index = 0
    is_balanced = True
    for i in range(len(parenthesis)):
        if parenthesis[i] in "({[" and is_balanced:
            s.push(parenthesis[i])
        elif s.is_empty():
            is_balanced = False
        else:
            top = s.pop()
            if not is_matched(top, parenthesis[i]):
                is_balanced = False
    if s.is_empty() and is_balanced:
        return True
    else:
        return False
    # while index < len(parenthesis) and is_balanced:
    #     paren = parenthesis[index]
    #     if paren in "({[":
    #         s.push(paren)
    #     else:
    #         if s.is_empty():
    #             is_balanced = False
    #         else:
    #             top = s.pop()
    #             if not is_matched(top, paren):
    #                 is_balanced = False
    #     index += 1
    # if s.is_empty() and is_balanced:
    #     return True
    # else:
    #     return False

s = Stack()
# s.push("A")
# s.push("B")
# s.push(1)
# print(s.get_stack())
# print(s.peek())
# print(s.is_empty())
# print(s.reverse_string("Hello"))s.get_stack()
# binary_representtion(242)
print(balanced_parenthesis("{{}}"))