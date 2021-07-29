# https://www.interviewbit.com/problems/partitions/


class Solution:
    def solve(self, l, arr):
        if l == 2:
            return 0
        from collections import defaultdict
        import operator
        from itertools import accumulate as acc
        d = defaultdict(int)
        d[arr[0]] = 1
        rightsum = list(acc(arr[::-1], operator.add))[::-1]
        leftsum = list(acc(arr, operator.add))
        result = 0
        for j in range(1, l - 1):
            temp = leftsum[j]
            if temp % 2:
                d[leftsum[j]] += 1
                continue
            middle = temp / 2
            if middle == rightsum[j + 1]:
                result += d[middle]
            d[leftsum[j]] += 1

        print(result)
        return result


s = Solution()
# arr = [1, 2, 3, 0, 3]
# arr = [1, -1, 0, 0]
# arr = [1, 0, 0, 0, 1, 1, 1, 0, 1, 1]
# arr = [ 3, 3, -3, 3, 3 ]
# s.solve(len(arr), arr)


# from random import randint
# l = randint(1, 100000)
# arr = [randint(-1000000000, 1000000000) for i in range(l)]
#
# # print(arr)
# print(l)
#
# s.solve(l, arr)