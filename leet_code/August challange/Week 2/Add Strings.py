# https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/614/week-2-august-8th-august-14th/3875/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p = len(num1) - 1
        q = len(num2) - 1

        result = ['0'] * (max(p + 1, q + 1) + 1)
        r = 0
        while p > -1 or q > -1:
            temp = int(result[r])
            n1 = n2 = 0
            if p > -1:
                n1 = int(num1[p])
            if q > -1:
                n2 = int(num2[q])
            result[r] = str((temp + n1 + n2) % 10)
            result[r + 1] = str((temp + n1 + n2) // 10)
            p -= 1
            q -= 1
            r += 1

        if result[-1] == '0':
            result.pop()

        return "".join(result[::-1])
