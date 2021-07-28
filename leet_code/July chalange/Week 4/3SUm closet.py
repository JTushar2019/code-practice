# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3828/


class Solution:
    def threeSumClosest(self, arr, target):
        import math
        i = 0
        l = len(arr)
        arr.sort()
        # print(arr)
        ans = (math.inf, -1)
        found = False
        temp = (math.inf, -1)

        for i in range(len(arr) - 2):
            k = i + 2
            for j in range(i + 1, l - 1):
                t = arr[i] + arr[j]
                while k < l:
                    t2 = arr[k] + t

                    if t2 < target:
                        k += 1
                    else:
                        if k - j > 1:
                            t3 = t2 - arr[k] + arr[k - 1]
                            temp = (abs(t3 - target), t3)
                            temp2 = (abs(t2 - target), t2)
                            temp = min(temp, temp2)
                        else:
                            temp = (abs(t2 - target), t2)
                        break
                else:
                    t3 = t + arr[k - 1]
                    temp = (abs(t3 - target), t3)

                if temp[0] < ans[0]:
                    ans = temp
                    # print(arr[i], arr[j], temp[1] - arr[i] - arr[j], k, " -> ", temp)

                if temp[0] == 0:
                    print("***********", ans[1], "***********")
                    return ans[1]

                if k - j == 1:
                    break
                else:
                    k -= 1

        print("***********", ans[1], "***********")
        return ans[1]


s = Solution()
from random import randint

arr = [randint(-1000, 1000) for i in range(1000)]
print(arr)
target = randint(-10000, 10000)
print(target)
s.threeSumClosest(arr, target)