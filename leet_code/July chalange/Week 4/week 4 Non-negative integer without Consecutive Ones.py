# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3826/
# https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/

import math

data = {}


class Solution:

    def utility(self, n):
        if n < 3:
            return 0
        elif n == 3:
            return 1

        if n in data:
            return data[n]

        k = math.ceil(math.log2(n + 1))
        p = 1 << (k - 1)
        q = (1 << (k - 1)) - 1
        r = (1 << (k - 2)) - 1

        print("p=", p, " q=", q, " r=", r)

        if str(bin(n))[3] == '1':
            data[n] = self.utility(q) + self.utility(r) + n - (r + p)
            return data[n]

        data[n] = self.utility(q) + self.utility(n - q - 1)
        return data[n]

    def findIntegers(self, n):
        return n - self.utility(n) + 1


s = Solution()
print(4)
print(s.utility(4))
print("**************************")
print(8)
print(s.utility(8))
print("**************************")
print(7)
print(s.utility(7))
print("**************************")
print(10)
print(s.utility(10))
print("**************************")
print(13)
print(s.utility(13))
print("**************************")
print(11)
print(s.utility(11))

print(data)