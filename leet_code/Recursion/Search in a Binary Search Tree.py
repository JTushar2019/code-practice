# https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/3233/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        
        p = self.searchBST(root.left,val)
        q = self.searchBST(root.right,val)
        if p:
            return p
        elif q:
            return q
        else:
            return None
        