# https://leetcode.com/explore/learn/card/recursion-i/255/recursion-memoization/1662/

class Solution:
    from functools import cache
    
    @cache
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)