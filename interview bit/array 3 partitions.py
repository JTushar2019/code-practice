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
        rightsum = list(acc(arr[::-1], operator.add))[::-1]  # left accumulating sum
        leftsum = list(acc(arr, operator.add))  # right accumulating sum
        result = 0
        for j in range(1, l - 1):
            temp = leftsum[j]
            if temp % 2:
                d[leftsum[j]] += 1
                continue
            middle = temp / 2
            # if sum till now is even.. it can be broken in 2 parts. left and middle partition
            # so breaking it into two parts. and check if the one part sum seen till now in hash
            # in left of j or
            # in my coding, default dict. it will give zero if key not present and add it in too.

            if middle == rightsum[j + 1]:  # if the broken portion is sum equal to right partition.
                result += d[middle]
                # doing this cause the broken half sum could be formed at different length

            d[leftsum[j]] += 1
            # also for current sum, add it to last seen value or if seen first time it will just do 0 + 1

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