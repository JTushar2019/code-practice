# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/612/week-5-july-29th-july-31st/3833/

class Solution:
    def trap(self, height):
        from itertools import accumulate as acc
        left = list(acc(height, max))
        right = list(acc(height[::-1], max))[::-1]
        water = 0
        print(left)
        print(right)
        for i in range(1, len(height) - 1):
            if left[i] and right[i]:
                water += min(right[i], left[i]) - height[i]
            print(left[i], right[i], water)
        print(water)
        return water


s = Solution()
s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
s.trap([4,2,0,3,2,5])