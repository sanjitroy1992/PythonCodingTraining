"""
In a Queue data structure, we maintain two pointers, front and rear. The front points the first item of queue and rear points to last item.

enQueue() This operation adds a new node after rear and moves rear to the next node. happens towards the right side.

deQueue() This operation removes the front node and moves front to the next node. happens towards the left side.
Link: https://www.geeksforgeeks.org/queue-linked-list-implementation/
"""
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# A class to represent a queue

# The queue, front stores the front node
# of LL and rear stores the last node of LL
class Queue:

    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    # Method to add an item to the queue
    def EnQueue(self, item):
        temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

        # Method to remove an item from queue

    def DeQueue(self):

        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next

        if (self.front == None):
            self.rear = None


# Driver Code
if __name__ == '__main__':
    q = Queue()
    q.EnQueue(10)
    q.EnQueue(20)
    q.DeQueue()
    q.DeQueue()
    q.EnQueue(30)
    q.EnQueue(40)
    q.EnQueue(50)
q.DeQueue()
print("Queue Front " + str(q.front.data))
print("Queue Rear " + str(q.rear.data))
