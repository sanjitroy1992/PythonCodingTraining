class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = Queue()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.enqueue(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        Pop method is costly here.
        get the size of the queue and run a for loop till size-1. if size=3 the only run the loop twice.
        dequeue item one by one with 0 index from the queue and enqueue it to the stack again
        finally the end the queue will have the last added element in the first position in the stack
        In the end pop that value using dequeue method and return it
        """
        for i in range(self.q.get_size() - 1):
            self.q.enqueue(self.q.dequeue())
        return self.q.dequeue()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q.items[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.q.size != 0:
            return False
        else:
            return True


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

s = MyStack()
s.push(1)
s.push(2)
s.push(3)
print(s.top())
print(s.empty())
s.pop()
print(s.top())
