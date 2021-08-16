# https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/615/week-3-august-15th-august-21st/3892/

class NumArray:

    def __init__(self, nums):
        l = s = len(nums)
        while s & (s - 1) != 0:
            s += 1
        self.arr = [0] * (2 * s)

        self.arr[s:s + l] = nums
        j = s - 1
        while j > 0:
            self.arr[j] = self.arr[2 * j] + self.arr[2 * j + 1]
            j -= 1

        self.offset = s

    def sumRange(self, left, right):

        sum = 0
        l = left + self.offset
        r = right + self.offset

        while l <= r:

            if l % 2 != 0:
                sum += self.arr[l]
                l += 1
            if r % 2 == 0:
                sum += self.arr[r]
                r -= 1

            l //= 2
            r //= 2

        return sum
