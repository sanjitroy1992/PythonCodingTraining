"""
Applications of Queue:
Queue is used when things don’t have to be processed immediately, but have to be processed in First InFirst Out order
like Breadth First Search. This property of Queue makes it also useful in following kind of scenarios.

1) When a resource is shared among multiple consumers. Examples include CPU scheduling, Disk Scheduling.
2) When data is transferred asynchronously (data not necessarily received at same rate as sent) between two processes.
Examples include IO Buffers, pipes, file IO, etc.

***Time Complexity:***
Time complexity of all operations like enqueue(), dequeue(), isFull(), isEmpty(), front() and rear() is O(1).
There is no loop in any of the operations.

Pros of Array Implementation
1. Easy to implement.

Cons of Array Implementation
1. Static Data Structure, fixed size.
2. If the queue has a large number of enqueue and dequeue operations, at some point we may not we able to insert
elements in the queue even if the queue is empty (this problem is avoided by using circular queue).
"""


class Queue():

    def __init__(self, capacity):
        self.items = []
        self.size = 0
        self.capacity = capacity

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            print("Full")
            return
        self.items.insert(0, item)
        print("Enqueued: {}".format(self.items[0]))
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Empty")
            return
        dequeue = self.items.pop()
        print("Dequeued: {}".format(dequeue))
        self.size -= 1

    def is_empty(self):
        return self.items == []

    def print_queue(self):
        print("->".join(self.items))

    def get_queue(self):
        return self.items

    def peek(self):
        return self.items[-1]

q = Queue(5)
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.enqueue("D")
q.enqueue("E")
q.enqueue("F")
q.print_queue()
q.dequeue()
print(q.get_queue())
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()


