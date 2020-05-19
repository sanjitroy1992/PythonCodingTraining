"""
In recursion, a function calls itself either directly or indirectly as a subroutine. As a result,
it requires less amount of code to perform the necessary tasks. Hence, considered one of the efficient methods
in programming. While writing a recursive function, we must keep in mind that it should have a base case and
the algorithm must change its state and move towards the base case.
Reference: https://www.codespeedy.com/reverse-a-queue-in-python/
"""


class Queue:
    def __init__(self):
        self.items = []

    def Empty(self):
        return self.items == []

    def enQueue(self, data):
        self.items.insert(0,data)

    def deQueue(self):
        return self.items.pop()

def Reverse():
    if(Q.Empty()):
        return
    temp = Q.data[-1]
    Q.deQueue()
    Reverse()
    Q.enQueue(temp)
Q = Queue()
Q.enQueue(5)
Q.enQueue(4)
Q.enQueue(3)
Q.enQueue(2)
Q.enQueue(1)
print(Q.data)
Reverse()
print(Q.data)