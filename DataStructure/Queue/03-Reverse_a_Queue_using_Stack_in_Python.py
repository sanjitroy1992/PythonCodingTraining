"""
Stack follows the last-in-first-out( LIFO ) principle. Similar to the Queue, the insert operation is called push and
remove operation as pop. In this method, we will dequeue the elements from the Queue and push them into the Stack.
Until the Queue becomes empty. Then we pop the elements from the Stack and enqueue them to the Queue
till the stack is empty. As a result, the elements in the Queue will be reversed.
Reference: https://www.codespeedy.com/reverse-a-queue-in-python/
"""
class Stack:
    def __init__(self):
        self.items = []

    def Empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()


class Queue:
    def __init__(self):
        self.items = []

    def Empty(self):
        return self.items == []

    def enQueue(self, data):
        self.items.insert(0, data)

    def deQueue(self):
        return self.items.pop()


def Reverse():
    while (not Q.Empty()):
        S.push(Q.deQueue())
    while (not S.Empty()):
        Q.enQueue(S.pop())


S = Stack()
Q = Queue()
Q.enQueue(5)
Q.enQueue(4)
Q.enQueue(3)
Q.enQueue(2)
Q.enQueue(1)
print(Q.items)
Reverse()
print(Q.items)