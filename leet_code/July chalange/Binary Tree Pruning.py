# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3824/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def foo(self, root):
        if not root:
            return -1

        left = self.foo(root.left)
        right = self.foo(root.right)

        if left == -1:
            root.left = None
        if right == -1:
            root.right = None

        if right == left == -1 and root.val == 0:
            return -1

        return root.val

    def pruneTree(self, root: TreeNode):
        self.foo(root)
        if root.val in (-1, None):
            return None

        return root