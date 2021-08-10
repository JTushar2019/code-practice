# https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/614/week-2-august-8th-august-14th/3876/

class Solution:
    def minFlipsMonoIncr(self, s):
        length = len(s)
        from itertools import accumulate as acc
        arr = list(acc(int(i) for i in s))

        result = arr[-1]
        i = length - 1
        while i > 0:
            result = min(result, 2 * arr[i - 1] + (length - i) - arr[-1])
            i -= 1
        result = min(result, length - arr[-1])
        print(result)
        return result

        # def utility(i, j, low='0', high='0'):
        #     nonlocal s
        #     # print("hello")
        #     if j < i:
        #         return 0
        #     if j == i:
        #         if low <= s[i] <= high:
        #             return 0
        #         else:
        #             return 1
        #
        #     if high == '0':
        #         # t = 0
        #         # for p in range(i, j + 1):
        #         #     if s[p] == '1':
        #         #         t += 1
        #         # return t
        #         if i > 0:
        #             return arr[j] - arr[i - 1]
        #         else:
        #             return arr[j]
        #
        #     elif low == '1':
        #         t = 0
        #         # for p in range(i, j + 1):
        #         #     if s[p] == '0':
        #         #         t += 1
        #         # return t
        #         if i > 0:
        #             return (j - i + 1) - (arr[j] - arr[i - 1])
        #         else:
        #             return (j - i + 1) - arr[j]
        #
        #     else:
        #         mid = (i + j) // 2
        #         t = 0
        #         if s[mid] == '0':
        #             r = utility(i, mid - 1, low, '0')
        #             p = utility(mid + 1, j, '0', high)
        #             t = r + p
        #             r = utility(i, mid - 1, low, '1')
        #             p = utility(mid + 1, j, '1', high)
        #             return min(t, 1 + r + p)
        #         else:
        #             r = utility(i, mid - 1, low, '0')
        #             p = utility(mid + 1, j, '0', high)
        #             t = r + p + 1
        #             r = utility(i, mid - 1, low, '1')
        #             p = utility(mid + 1, j, '1', high)
        #             return min(t, r + p)
        #
        # p = utility(0, length - 1, '0', '1')
        # print(p)
        # return p


from random import randint

r = "".join([str(randint(0, 1)) for p in range(100000)])
# print(r)
s = Solution()
s.minFlipsMonoIncr(r)
