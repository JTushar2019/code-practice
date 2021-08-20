# https://leetcode.com/explore/learn/card/recursion-i/253/conclusion/2384/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def foo(i,j):
            if i > j:
                return [None]
            ans = []
            for each in range(i,j+1):
                left = foo(i,each-1)
                right = foo(each+1,j)
                
                for l in left:
                    for r in right:
                        root = TreeNode(each)
                        root.left = l
                        root.right = r
                        ans.append(root)
            return ans
        
        return foo(1,n)