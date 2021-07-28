# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        p1 = l1
        p2 = l2
        carry = 0

        start = p3 = ListNode(0)
        previous = None
        while p1 or p2:
            temp2 = temp1 = 0
            if p1:
                temp1 = p1.val
                p1 = p1.next
            if p2:
                temp2 = p2.val
                p2 = p2.next

            node = ListNode((temp1 + temp2 + p3.val) // 10)
            p3.val = (temp1 + temp2 + p3.val) % 10
            p3.next = node
            previous = p3
            p3 = node

        if p3.val == 0:
            previous.next = None

        return start