# https://leetcode.com/explore/learn/card/recursion-i/253/conclusion/1675/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        if n == 1:
            return 0
        mid = 1 << (n-2)
        
        if k <= mid:
            return self.kthGrammar(n-1,k)
        else:
            if self.kthGrammar(n-1,k - mid):
                return 0
            else:
                return 1
        