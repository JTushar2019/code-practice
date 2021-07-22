# https://leetcode.com/problems/validate-binary-search-tree/

# Definition
# for a binary tree node.
#
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # def inorderTraverser(self, root, l):
    #     if not root:
    #         return
    #     self.inorderTraverser(root.left, l)
    #
    #     l.append(root.val)
    #
    #     self.inorderTraverser(root.right, l)
    #
    # def isValidBST(self, root: TreeNode) -> bool:
    #
    #     l = []
    #     self.inorderTraverser(root, l)
    #
    #     for i in range(1,len(l)):
    #         if l[i] < l[i-1]:
    #             return False
    #
    #     return True

    # *************************************"better and concise approach"******************************
    def isValidBST(self, root: TreeNode) -> bool:

        def validate(node, low=-math.inf, high=math.inf):
            # Empty trees are valid BSTs.
            if not node:
                return True
            # The current node's value must be between low and high.
            if node.val <= low or node.val >= high:
                return False

            # The left and right subtree must also be valid.
            return (validate(node.right, node.val, high) and
                    validate(node.left, low, node.val))

        return validate(root)