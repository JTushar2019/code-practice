# https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def foo(num, power):
            if power == 0:
                return 1
            prod = 1
            if abs(power) % 2 == 1:
                if power > 0:
                    prod = num
                    power -= 1
                else:
                    prod /= num
                    power += 1
            prod = foo(num, power//2)**2 * prod
            return prod
        return foo(x,n)
        