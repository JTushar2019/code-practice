# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3823/

class Solution:
    def partitionDisjoint(self, nums) -> int:
        import heapq as hp
        l = [(nums[i], i) for i in range(len(nums))]
        hp.heapify(l)
        ans = 0
        j = 0
        while j <= ans:
            while l and nums[j] > l[0][0]:
                temp = hp.heappop(l)[1]
                ans = max(ans, temp)
            j += 1
        ans += 1
        return ans


s = Solution()
print(s.partitionDisjoint([5, 0, 3, 8, 6, 9]))
print(s.partitionDisjoint([3, 10, 0, 5, 8, 6]))
print(s.partitionDisjoint([1, 1, 1, 0, 6, 12]))
print(s.partitionDisjoint([1, 1, 1]))
print(s.partitionDisjoint([26, 51, 40, 58, 42, 76, 30, 48, 79, 91]))
print(s.partitionDisjoint([6, 0, 8, 30, 37, 6, 75, 98, 39, 90, 63, 74, 52, 92, 64]))