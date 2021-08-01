# https://leetcode.com/problems/range-sum-query-immutable/

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

    # def sumRange(self, left, right):
    #
    #     def foo(node, nlow, nhigh, left, right):
    #
    #         if left <= nlow and nhigh <= right:
    #             return self.segtrees[node]
    #         if nhigh < left or right < nlow:
    #             return 0
    #
    #         mid = (nlow+nhigh) // 2
    #         print(mid)
    #         return foo(2 * node, nlow, mid, left, right) + \
    #                foo(2 * node + 1, mid + 1, nhigh, left, right)
    #
    #     return foo(1, 0, self.length - 1, left, right)


# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
left = 0
right = 2
param_1 = obj.sumRange(left, right)
print(param_1)