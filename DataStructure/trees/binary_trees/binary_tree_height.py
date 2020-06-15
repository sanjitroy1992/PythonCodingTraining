class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Binary_Tree(object):
    def __init__(self, root):
        self.root = Node(root)

    def height(self, root):
        if not root:
            return 0
        else:
            return self._height(root, 0)

    def _height(self, cur_node, cur_height):
        if not cur_node:
            return cur_height
        left_height = self._height(cur_node.left, cur_height + 1)
        right_height = self._height(cur_node.right, cur_height + 1)
        return max(left_height, right_height)

tree = Binary_Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
print(tree.height(tree.root))