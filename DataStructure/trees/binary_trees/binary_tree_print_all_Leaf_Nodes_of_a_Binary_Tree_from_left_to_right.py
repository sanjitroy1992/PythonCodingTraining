"""
Input :
           1
          /  \
         2    3
        / \  / \
       4  5  6  7

Output :4 5 6 7

Approach:The idea is to use two stacks, one to store all the nodes of the tree and the other one to store all the leaf nodes.
We will pop the top node of the first stack.
If the node has a left child, we will push it on top of the first stack,
if it has a right child then we will push it onto the top of the first stack,
but if the node is a leaf node then we will push it onto the top of the second stack.
We will do it for all the nodes until we have traversed the Binary tree completely.

Then we will start popping the second stack and print all its elements until the stack gets empty.

Below is the implementation of the above approach:
"""


# Python3 program to print all the leaf
# nodes of a Binary tree from left to right

# Binary tree node
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to Print all the leaf nodes
# of Binary tree using two stacks
def PrintLeafLeftToRight(root):
    # Stack to store all the nodes
    # of tree
    s1 = []

    # Stack to store all the
    # leaf nodes
    s2 = []

    # Push the root node
    s1.append(root)

    while len(s1) != 0:
        curr = s1.pop()

        # If current node has a left child
        # push it onto the first stack
        if curr.left:
            s1.append(curr.left)

        # If current node has a right child
        # push it onto the first stack
        if curr.right:
            s1.append(curr.right)

        # If current node is a leaf node
        # push it onto the second stack
        elif not curr.left and not curr.right:
            s2.append(curr)

        # Print all the leaf nodes
    while len(s2) != 0:
        print(s2.pop().data, end=" ")


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(7)
    root.left.left.left = Node(10)
    root.left.left.right = Node(11)
    root.right.right.left = Node(8)

    PrintLeafLeftToRight(root)