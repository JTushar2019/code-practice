# https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/

class Solution:
    def minNonZeroProduct(self, n: int) -> int:
        if n == 1:
            return 1
        modulator = 10**9 + 7
        def foo(num, power):
            nonlocal modulator 
            if power == 1:
                return num
            prod = 1
            if power % 2 == 1:
                prod = num
                power -= 1
            prod = ((((foo(num, power//2))**2) %
                    modulator) * prod) % modulator
            return prod
        
        numer = ((1 << n) - 2) % modulator
        power = (1 << (n-1)) - 1
        t = foo(numer, power)
        t = (t * ((1 << n) - 1) % modulator) % modulator
        
        return t