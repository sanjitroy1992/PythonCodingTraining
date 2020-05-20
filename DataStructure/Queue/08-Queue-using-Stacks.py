"""
This method makes sure that oldest entered element is always at the top of stack 1, so that deQueue operation just pops from stack1. To put the element at top of stack1, stack2 is used.

enQueue(q, x):

While stack1 is not empty, push everything from stack1 to stack2.
Push x to stack1 (assuming size of stacks is unlimited).
Push everything back to stack1.
Here time complexity will be O(n)

deQueue(q):

If stack1 is empty then error
Pop an item from stack1 and return it
Here time complexity will be O(1)
"""


# Python3 program to implement Queue using
# two stacks with costly enQueue()

class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self, x):

        # Move all elements from s1 to s2
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()

        # Push item into self.s1
        self.s1.append(x)

        # Push everything back to s1
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

        # Dequeue an item from the queue

    def deQueue(self):

        # if first stack is empty
        if len(self.s1) == 0:
            print("Q is Empty")

        # Return top of self.s1
        x = self.s1[-1]
        self.s1.pop()
        return x

    # Driver code


if __name__ == '__main__':
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)

    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
