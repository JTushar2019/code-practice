# https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/615/week-3-august-15th-august-21st/3903/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        d = {None:0}
        answer = 0

        def sumer(node):
            nonlocal d
            if not node:
                return 0
            d[node] = sumer(node.left) + sumer(node.right) + node.val
            return d[node]

        def foo(s, node):
            nonlocal answer, d
            s += node.val
            p1 = p2 = 0
            if node.left:
                p1 = d[node.left] * (s + d[node.right])
                foo(s + d[node.right], node.left)
            if node.right:
                p2 = d[node.right] * (s + d[node.left])
                foo(s + d[node.left], node.right)

            answer = max(answer, p1, p2)



        sumer(root)
        foo(0, root)
        return answer
