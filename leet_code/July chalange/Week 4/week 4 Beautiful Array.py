# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3829/
# https://leetcode.com/problems/beautiful-array/

class Solution:
    def beautifulArray(self, n):
        arr = list(range(1, n + 1))
        import math

        def foo(arr, i, j):
            if j - i <= 1:
                return

            leftsubarray = arr[i:j:2]
            rightsubarray = arr[i + 1:j:2]
            l = math.ceil((j - i) / 2)
            r = j - i - l
            arr[i:j] = leftsubarray + rightsubarray
            print("left = ", leftsubarray, "Range =", (i, i + l))
            print("right = ", rightsubarray, "Range =", (i + l, j))

            foo(arr, i, i + l)
            foo(arr, i + l, j)

        foo(arr, 0, n)
        print(arr)
        return arr


s = Solution()
s.beautifulArray(10)