"""
run a for loop to enqueue the items into the queue and then dequeue one by one item and add to rev string.
Time Complexity: Linear time - O(n)
"""


class Queue:

    def __init__(self):
        self.items = []
    def enqueu(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def is_empty(self):
        return self.items==[]
    def print_queue(self):
        for i in self.items:
            print(i)
    def get_queue(self):
        return self.items
    def peek(self):
        return self.items[-1]

def reverse(queue, input_string=None):
    for i in range(len(input_string)):
        queue.enqueu(input_string[i])
    rev = ''
    while not queue.is_empty():
        rev = queue.dequeue() + rev
    return rev


Q = Queue()
print(reverse(Q, "Hello"))