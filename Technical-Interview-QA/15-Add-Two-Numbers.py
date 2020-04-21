"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
l1 = 243
l2 = 564
def revnum(num):
    rev = 0
    while num != 0:
        rem = num % 10
        num = num//10
        rev = (rev*10) + rem
    return rev

def addTwoNumbers(l1, l2):
    l1_rev = revnum(l1)
    l2_rev = revnum(l2)
    return l1_rev+l2_rev

print(addTwoNumbers(l1,l2))