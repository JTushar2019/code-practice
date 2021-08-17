# https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/615/week-3-august-15th-august-21st/3899/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, node):
        def utility(node, val):
            if not node:
                return 0
            ans = 0
            if node.val >= val:
                ans += 1
            val = max(val, node.val)
            ans += utility(node.left, val)
            ans += utility(node.right, val)

            return ans

        return utility(node, node.val)
