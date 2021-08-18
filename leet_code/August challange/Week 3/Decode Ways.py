# https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/615/week-3-august-15th-august-21st/3902/

class Solution:
    def numDecodings(self, s):
        l = len(s)
        # if s[0] == '0':
        #     return 0
        # from functools import cache
        #
        # @cache
        # def foo(n):
        #     nonlocal s, l
        #
        #     if n == l - 1:
        #         if s[n] != '0':
        #             return 1
        #         return 0
        #     if n == l:
        #         return 1
        #
        #     total = 0
        #     if n < l and '0' < s[n]:
        #         total += foo(n + 1)
        #     if n < l - 1 and 10 <= int(s[n:n + 2]) < 27:
        #         total += foo(n + 2)
        #     return total
        #
        # return foo(0)

        arr = [0] * (l + 1)
        arr[l] = 1
        if s[l-1] != '0':
            arr[l-1] = 1
        for i in range(l - 2, -1, -1):
            if s[i] != '0':
                arr[i] += arr[i + 1]

                if 10 <= int(s[i:i + 2]) < 27:
                    arr[i] += arr[i + 2]

        print(arr)
        return arr[0]

s = Solution()
print(s.numDecodings("2"))
print(s.numDecodings("226"))
print(s.numDecodings("06"))
print(s.numDecodings("1201"))
print(s.numDecodings("10"))
