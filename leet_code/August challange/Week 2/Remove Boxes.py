# https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/614/week-2-august-8th-august-14th/3889/


class Solution:
    def removeBoxes(self, boxes):
        from functools import cache

        @cache
        def foo(i, j, k):
            if i > j:
                return 0
            while i < j and boxes[i] == boxes[i + 1]:
                i += 1
                k += 1
            temp = (k + 1) ** 2 + foo(i + 1, j, 0)
            for p in range(i + 1, j + 1):
                if boxes[p] == boxes[i]:
                    temp = max(temp, foo(i + 1, p - 1, 0) + foo(p, j, k + 1))

            return temp

        return foo(0, len(boxes) - 1, 0)


