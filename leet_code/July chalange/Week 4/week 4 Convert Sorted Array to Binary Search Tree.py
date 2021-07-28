# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3827/
# https://leetcode.com/problems/binary-tree-pruning/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        def utility(i, j):
            nonlocal nums

            if j - i + 1 == 1:
                return TreeNode(nums[i])
            if i > j:
                return None

            mid = (i + j) // 2

            left = utility(i, mid - 1)
            right = utility(mid + 1, j)

            node = TreeNode(nums[mid])
            node.left = left
            node.right = right
            return node

        return utility(0, len(nums) - 1)