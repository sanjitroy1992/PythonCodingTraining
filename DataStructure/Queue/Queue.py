class Queue():
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

q = Queue()
q.enqueu("A")
q.enqueu("B")
q.enqueu("C")
q.print_queue()
q.dequeue()
print(q.get_queue())

