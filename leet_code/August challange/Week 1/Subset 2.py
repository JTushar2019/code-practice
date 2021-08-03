# https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/613/week-1-august-1st-august-7th/3837/

class Solution:
    def subsetsWithDup(self, nums):
        result = set()
        arr = []
        l = len(nums)
        nums.sort()

        def utility(i):
            nonlocal nums, arr, l
            if i == l:
                result.add(tuple(arr[:]))
                print(arr)
                return

            arr.append(nums[i])
            utility(i + 1)
            arr.pop()
            utility(i + 1)

        utility(0)

        return result


s = Solution()
s.subsetsWithDup([1, 2, 6, 4, 4, 4, 2])