# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def print_list(self):
#         cur_node = self.head
#         while cur_node:
#             print(cur_node.data)
#             cur_node = cur_node.next
#
#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         last_node = self.head
#         while last_node.next:
#             last_node = last_node.next
#         last_node.next = new_node
#     def prepend(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
#     def insert_node(self,prev_data, data):
#         if not prev_data:
#             print("previous node does not exist")
#             return
#         new_node = Node(data)
#         new_node.next = prev_data.next
#         prev_data.next = new_node
#
# llist = LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")
# # llist.prepend('E')
# # print(llist.head.next.data)
# llist.insert_node(llist.head.next, 'E')
# llist.print_list()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


list1 = LinkedList()
list1.append("A")
list1.append("B")
list1.print()