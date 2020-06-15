import sys
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Binary_Tree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, type):
        if type == "inorder":
            return self.inorder_print(tree.root, "")
        elif type == "preorder":
            return self.preorder_print(tree.root, "")
        elif type == "postorder":
            return self.postorder_print(tree.root, "")

    def inorder_print(self, start, traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def preorder_print(self, start, traversal):
        """Root->left->Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

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

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        # if value is less than the cur node value and cur node left value is present then do a recursive call
        # when the left next node is empty crate a new node with the value
        # do the same for right side
        if value<cur_node.value:
            if not cur_node.left:
                cur_node.left = Node(value)
            else:
                self._insert(value, cur_node.left)
        elif value>cur_node.value:
            if not cur_node.right:
                cur_node.right = Node(value)
            else:
                self._insert(value, cur_node.right)

    def inorder_tree(self, root):
        if root:
            self._inorder_tree(root)

    def _inorder_tree(self, cur_node):
        if cur_node:
            self._inorder_tree(cur_node.left)
            print(cur_node.value)
            self._inorder_tree(cur_node.right)

    def search(self, value):
        if not self.root:
            return False
        else:
            return self._search(self.root, value)

    def _search(self, cur_node, value):
        if cur_node.value == value:
            return True
        # if value is less than the cur node value and cur node left value is not none then do a recursive call and return
        # do the same for right side
        # else return False
        elif value<cur_node.value and cur_node.left:
            return self._search(cur_node.left, value)
        elif value>cur_node.value and cur_node.right:
            return self._search(cur_node.right, value)
        return False

    def validate_bst(self, cur_node, min =-sys.maxsize, max =sys.maxsize):
        # here we have taken highest minimum and maximum value
        if not cur_node:
            return True
        # 4 conditions has to be validated and true.
        # cur_node has to be greater than minimum value and lesser than cur node value.
        # recursive call for both left and right side
        if (cur_node.value>min
                and cur_node.value<max
                and self.validate_bst(cur_node.left, min, cur_node.value)
                and self.validate_bst(cur_node.right, cur_node.value, max)):
            return True
        else:
            return False

    def size(self, root):
        if not root:
            return 0
        else:
            # add 1 for the root node + left children + right children
            return 1 +self.size(root.left) + self.size(root.right)



tree = Binary_Tree(10)
# tree.root.left = Node(5)
# tree.root.right = Node(15)
# tree.root.left.left = Node(2)
# tree.root.left.right = Node(7)
# tree.root.right.left = Node(12)
# tree.root.right.right = Node(17)
# print(tree.print_tree("inorder"))
# print(tree.print_tree("preorder"))
# print(tree.print_tree("postorder"))
# print(tree.height(tree.root))

tree.insert(8)
tree.insert(12)
# tree.insert(9)
# tree.insert(7)
# tree.insert(13)
# tree.insert(11)
# print(tree.inorder_tree(tree.root))
# # print(tree.search(9))
print(tree.height(tree.root))
print(tree.inorder_print(tree.root, ""))
# print(tree.validate_bst(tree.root))
print(tree.size(tree.root))

