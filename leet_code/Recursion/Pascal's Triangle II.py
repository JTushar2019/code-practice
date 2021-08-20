# https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/3234/

class Solution:
    def getRow(self, n: int) -> List[int]:
        
        def foo(n,l,prr):
            n -= 1
            l += 1
            arr = [1]*l
            for i in range(1,l-1):
                arr[i] = prr[i] + prr[i-1]
            if n == 0:
                return arr
            else:
                return foo(n,l,arr)
            
        return foo(n+1,0,[])
            
        