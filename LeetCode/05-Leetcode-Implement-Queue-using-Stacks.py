"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while (len(self.s1) != 0):
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while (len(self.s2) != 0):
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while (len(self.s1) != 0):
            return self.s1.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.s1[-1]

    def get_queue(self):
        """
        Get the queue elements.
        """
        if not (len(self.s1)==0):
            return self.s1
        else:
            raise AssertionError("Queue is Empty")

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.s1) == 0:
            return True
        else:
            return False

#Your MyQueue object will be instantiated and called as such:
q = MyQueue()
q.push(1)
q.push(2)
print(q.get_queue())
q.pop()
print(q.peek())
print(q.empty())
q.pop()
print(q.empty())