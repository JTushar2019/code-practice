# https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/613/week-1-august-1st-august-7th/3835/
# https://leetcode.com/problems/making-a-large-island/


class Solution:
    def largestIsland(self, grid):
        answer = 0
        n = len(grid) - 1
        l = n + 1
        k = 1

        def dfs(i, j):
            nonlocal grid, answer
            if grid[i][j] in (0, k):
                return 0

            if grid[i][j] == 1:
                grid[i][j] = k
                temp = 1
                if i > 0:
                    temp += dfs(i - 1, j)
                if i < n:
                    temp += dfs(i + 1, j)
                if j > 0:
                    temp += dfs(i, j - 1)
                if j < n:
                    temp += dfs(i, j + 1)

                return temp

        disjoint_set = {}
        for p in range(l):
            for q in range(l):
                if grid[p][q] == 1:
                    k += 1
                    disjoint_set[k] = max(answer, dfs(p, q))

        if disjoint_set:
            answer = max(disjoint_set.values())

        for i in range(l):
            for j in range(l):
                if grid[i][j] == 0:
                    d = set()
                    if i > 0 and grid[i - 1][j] > 1:
                        d.add(grid[i - 1][j])
                    if i < n and grid[i + 1][j] > 1:
                        d.add(grid[i + 1][j])
                    if j > 0 and grid[i][j - 1] > 1:
                        d.add(grid[i][j - 1])
                    if j < n and grid[i][j + 1] > 1:
                        d.add(grid[i][j + 1])

                    temp = 1
                    for each in d:
                        temp += disjoint_set[each]
                    answer = max(answer, temp)

        answer = max(1, answer)
        print(answer)

        return answer