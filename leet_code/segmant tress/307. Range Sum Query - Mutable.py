# https://leetcode.com/problems/range-sum-query-mutable/
class NumArray:

    def __init__(self, nums):
        size = len(nums)
        self.length = size

        while size & size - 1 != 0:
            size += 1
        self.segtrees = [0] * (2 * size)
        self.segtrees[size:size + self.length] = nums

        for i in range(size - 1, 0, -1):
            self.segtrees[i] = self.segtrees[2 * i] + self.segtrees[2 * i + 1]

        self.length = size

    def sumRange(self, left, right):

        sum = 0
        l, r = self.length + left, self.length + right
        while l <= r:

            if l % 2:  # right child
                sum += self.segtrees[l]
                l += 1

            if not r % 2:  # left child
                sum += self.segtrees[r]
                r -= 1

            l //= 2
            r //= 2
        return sum

    def update(self, index, val):

        self.segtrees[index + self.length] = val
        node = (self.length + index) // 2
        while node:
            self.segtrees[node] = self.segtrees[2 * node] + self.segtrees[2 * node + 1]
            node //= 2