# https://leetcode.com/problems/subarrays-with-k-different-integers/


def subarraysWithKDistinct(nums, k):
    from collections import defaultdict
    i = 0
    d = defaultdict(int)
    ans = 0
    j = 0
    l = len(nums)

    def virtual_expander():
        # this virtually expands j and tries to find good subarray with current k distinct
        nonlocal ans, i, d, j
        p = j + 1
        if d[nums[i]] > 1:
            while p < l and nums[p] in d:
                ans += 1
                p += 1

    def window_contractor():
        # this increments i till it can be done while maintaining the count of k distinct
        # and for each increment it will call virtual expander too.
        nonlocal ans, i, d, j
        while d[nums[i]] > 1:
            d[nums[i]] -= 1
            i += 1
            ans += 1
            virtual_expander()

    while j < l:
        d[nums[j]] += 1
        if len(d) == k:
            ans += 1
            virtual_expander()
            window_contractor()

        while len(d) > k:
            d[nums[i]] -= 1
            if d[nums[i]] == 0:
                d.pop(nums[i])
                ans += 1
                i += 1
                virtual_expander()
                window_contractor()
                break
            i += 1
        j += 1
    return ans


print(subarraysWithKDistinct(nums=[1, 2, 1, 3, 4], k=3))
print(subarraysWithKDistinct(nums=[1, 2, 1, 2, 3], k=2))
print(subarraysWithKDistinct([2, 2, 1, 2, 2, 2, 1, 1], 2))
print(subarraysWithKDistinct(
    [27, 27, 43, 28, 11, 20, 1, 4, 49, 18, 37, 31, 31, 7, 3, 31, 50, 6, 50, 46, 4, 13, 31, 49, 15, 52, 25, 31, 35, 4,
     11, 50, 40, 1, 49, 14, 46, 16, 11, 16, 39, 26, 13, 4, 37, 39, 46, 27, 49, 39, 49, 50, 37, 9, 30, 45, 51, 47, 18,
     49, 24, 24, 46, 47, 18, 46, 52, 47, 50, 4, 39, 22, 50, 40, 3, 52, 24, 50, 38, 30, 14, 12, 1, 5, 52, 44, 3, 49, 45,
     37, 40, 35, 50, 50, 23, 32, 1, 2], 20))