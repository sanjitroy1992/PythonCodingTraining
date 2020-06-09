class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
                cur_node.left.parent = cur_node
            else:
                self._insert(data, cur_node.left)

        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
                cur_node.right.parent = cur_node
            else:
                self._insert(data, cur_node.right)
        else:
            print("Value already in tree!")

    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
        else:
            return None

    def _find(self, data, cur_node):
        if data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        if data == cur_node.data:
            return True

    def inorder_print_tree(self):
        """
            Inorder (Left, Root, Right)
        """
        if self.root:
            self._inorder_print_tree(self.root)

    def _inorder_print_tree(self, cur_node):
        if cur_node:
            self._inorder_print_tree(cur_node.left)
            print(str(cur_node.data))
            self._inorder_print_tree(cur_node.right)

    def preorder_print_tree(self):
        """
            Preorder (Root, Left, Right)
        """
        if self.root:
            self._preorder_print_tree(self.root)

    def _preorder_print_tree(self, cur_node):
        if cur_node:
            print(str(cur_node.data))
            self._preorder_print_tree(cur_node.left)
            self._preorder_print_tree(cur_node.right)

    def postorder_print_tree(self):
        """
        Inorder(Right, Root, Left)
        """
        if self.root:
            self._postorder_print_tree(self.root)

    def _postorder_print_tree(self, cur_node):
        if cur_node:
            self._postorder_print_tree(cur_node.right)
            print(str(cur_node.data))
            self._postorder_print_tree(cur_node.left)


bst = BST()
bst.insert(4)
bst.insert(2)
bst.insert(5)
bst.insert(1)
bst.insert(3)

print(bst.find(11))
# bst.inorder_print_tree()
# bst.preorder_print_tree()
bst.postorder_print_tree()