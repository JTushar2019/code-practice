# https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/613/week-1-august-1st-august-7th/3838/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root, target):
        temp = target
        arr = []
        final = []

        def utility(node, result):
            nonlocal target, arr
            if not node:
                return

            arr.append(node.val)
            result += node.val

            if result == target and not node.left and not node.right:
                final.append(arr[:])

            utility(node.left, result)
            utility(node.right, result)

            arr.pop()
            result -= node.val

        utility(root, 0)

        return final