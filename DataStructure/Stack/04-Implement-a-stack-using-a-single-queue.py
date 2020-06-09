"""
1. Create a class Queue.
2. Define methods enqueue, dequeue, is_empty and get_size inside the class Queue.
3. Create a class Stack with instance variable q initialized to an empty queue.
4. Pushing is done by enqueuing data to the queue.
5. To pop, the queue is dequeued and enqueued with the dequeued element n – 1 times where n is the size of the queue.
This causes the the last element added to the queue to reach the rear of the queue.
The queue is dequeued one more time to get the item to be returned.
6. The method is_empty returns True if the queue is empty.
"""
class Stack:
    def __init__(self):
        self.q = Queue()

    def is_empty(self):
        return self.q.is_empty()

    def push(self, data):
        self.q.enqueue(data)

    def pop(self):
        print("original q: {}".format(self.q.get_queue()))
        for i in range(self.q.get_size() - 1):
            print(i)
            # dequeued = self.q.dequeue()
            # print("after q: {}".format(self.q.get_queue()))
            # print("dequeued value: {}".format(dequeued))
            self.q.enqueue(self.q.dequeue())
            print("enqueue: {}".format(self.q.get_queue()))
        return self.q.dequeue()


class Queue:
    def __init__(self):
        self.items = []
        self.size = 0

    def is_empty(self):
        return self.items == []

    def enqueue(self, data):
        self.size += 1
        self.items.append(data)

    def dequeue(self):
        self.size -= 1
        return self.items.pop(0)

    def get_size(self):
        return self.size

    def get_queue(self):
        return self.items


s = Stack()

print('Menu')
print('push <value>')
print('pop')
print('quit')

while True:
    do = input('What would you like to do? ').split()

    operation = do[0].strip().lower()
    if operation == 'push':
        s.push(int(do[1]))
    elif operation == 'pop':
        if s.is_empty():
            print('Stack is empty.')
        else:
            print('Popped value: ', s.pop())
    elif operation == 'quit':
        break