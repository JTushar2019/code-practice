# https://leetcode.com/explore/learn/card/recursion-i/255/recursion-memoization/1661/

class Solution:
    from functools import cache
    @cache
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)