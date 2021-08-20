# https://leetcode.com/explore/learn/card/recursion-i/250/principle-of-recursion/1440/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        def foo(p,q):
            nonlocal s
            if p>=q:
                return 
            s[p],s[q] = s[q],s[p]
            foo(p+1,q-1)

            
            
        foo(0,len(s)-1)