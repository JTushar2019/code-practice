# https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/

class Solution:
    def minimumTimeRequired(self, jobs, k):
        import math
        work = [0] * k
        l = len(jobs)
        s = math.ceil(l / k)
        jobs.sort(reverse=True)
        answer = 0
        for i in range(s):
            answer += jobs[i]

        def sol(distinct_worker, size, zeros, workmax):
            nonlocal work, k, answer

            if size == 0:
                print(work)
                answer = min(answer, workmax)
                return

            temp = jobs[size - 1]
            size -= 1
            for j in range(distinct_worker):

                if work[j] + temp >= answer:
                    continue

                if work[j] == 0:
                    zeros -= 1

                work[j] += temp

                t = workmax
                if work[j] > workmax:
                    t = work[j]

                if zeros <= size:
                    if distinct_worker < k:
                        sol(distinct_worker + 1, size, zeros, t)
                    else:
                        sol(distinct_worker, size, zeros, t)

                work[j] -= temp

                if work[j] == 0:
                    zeros += 1
            size += 1

        sol(distinct_worker=1, size=l, zeros=k, workmax=0)
        print("***********", answer, "**********")

        return answer


s = Solution()
from random import randint

s.minimumTimeRequired([3],
                      1)

# arr = [randint(1, 100) for i in range(12)]
# print(arr)
arr = [34, 45, 40, 52, 69, 61, 87, 20, 26, 81, 49, 50]
s.minimumTimeRequired(arr, 9)

# s.minimumTimeRequired(
#     [9899456, 8291115, 9477657, 9288480, 5146275, 7697968, 8573153, 3582365, 3758448, 9881935, 2420271, 4542202],
#     9)