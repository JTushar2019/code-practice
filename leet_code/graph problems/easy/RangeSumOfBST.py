# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def inorder_traverser(self, root, l, range):
        if not root:
            return

        self.inorder_traverser(root.left, l, range)

        if range[0] <= root.val <= range[1]:
            l[0] += root.val

        self.inorder_traverser(root.right, l, range)

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        l = [0, False]
        range = (low, high)
        self.inorder_traverser(root, l, range)
        return l[0]