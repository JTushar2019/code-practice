# https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/2378/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p , q = None, head
        while q:
            temp = q.next
            q.next = p
            p = q
            q = temp
        return p
    
#         if not head:
#             return None
        
#         if head.next:
#             first = head
#             t = self.reverseList(head.next)
#             p = t
#             while p.next :
#                 p = p.next
#             p.next = first
#             first.next = None
#             return t
#         else:
#             return head
        
