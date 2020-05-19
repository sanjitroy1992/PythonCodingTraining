# A simple implementation of Priority Queue
# using Queue.

class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def insert(self, data):
        self.queue.insert(0,data)

    # for popping an element based on Priority
    def priority(self):
        self.queue.sort()
        while self.queue:
            print(self.queue.pop())


if __name__ == '__main__':
    myQueue = PriorityQueue()
    myQueue.insert([3,"C"])
    myQueue.insert([2,"B"])
    myQueue.insert([1,"A"])
    myQueue.insert([4,"D"])
    print(myQueue)
    print(myQueue.priority())