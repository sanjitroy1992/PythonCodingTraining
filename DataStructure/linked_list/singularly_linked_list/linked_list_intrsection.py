"""
Let's say there are two linked lists. one with headA and another one with headB.
Solution:
0. check if both the nodes are None or not.
1. traverse from head of the first linked list with headA till it is None.
2. then once it is None assign it to headB.
3. do the same for second linked list head B.
4. then increment by one step at a time.
5. the moment they meet return the node data.
"""
def LL_Intersection(headA, headB):
    if not (headA and headB):
        return False
    first_node = headA
    second_node = headB
    while(first_node.data != second_node.data):
        if first_node.data == None:
            first_node = headB
        else:
            first_node = first_node.next
        if second_node.data == None:
            second_node = headA
        else:
            second_node = second_node.next

    return first_node.data

