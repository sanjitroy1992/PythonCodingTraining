"""
Given a queue. The task is to reverse the queue using another another empty queue.

Examples:

Input: queue[] = {1, 2, 3, 4, 5}
Output: 5 4 3 2 1

Input: queue[] = {10, 20, 30, 40}
Output: 40 30 20 10

Approach:
Given a queue and an empty queue.
The last element of the queue should be the first element of the new queue.
To get the last element there is a need to pop the queue one by one and add it to the end of the queue, size – 1 times.
So after that, we will get the last element in front of the queue. Now pop that element out and add it to the new queue.
Repeat the steps s – 1 times where s is the original size of the queue.
"""

# Python3 implementation of the above approach
from collections import deque

# Function to return the reversed queue
def reverse(q):
    # Size of ueue
    s = len(q)

    # Second queue
    ans = deque()

    for i in range(s):

        # Get the last element to the
        # front of queue
        for j in range(s - 1):
            x = q.popleft()
            q.appendleft(x)

        # Get the last element and
        # add it to the new queue
        ans.appendleft(q.popleft())
    return ans


# Driver Code
q = deque()

# Insert elements
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)

q = reverse(q)

# Print the queue
while (len(q) > 0):
    print(q.popleft(), end=" ")