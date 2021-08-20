# https://leetcode.com/explore/learn/card/recursion-i/250/principle-of-recursion/1681/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        head.val, head.next.val = head.next.val, head.val
        self.swapPairs(head.next.next)
        return head
        