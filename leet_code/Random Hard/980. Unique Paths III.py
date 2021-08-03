# https://leetcode.com/problems/unique-paths-iii/

class Solution:
    def uniquePathsIII(self, grid):
        m = len(grid)
        n = len(grid[0])
        ans = 0
        obstacles = 0
        x = y = 0
        hx = hy = 0

        def utility(i, j, todo):
            nonlocal grid, m, n, ans, hx, hy

            if i == hx and j == hy:
                if todo == -1:
                    ans += 1
                return
            if todo < -1:
                return

            grid[i][j] = -1
            if i > 0 and grid[i - 1][j] != -1:
                utility(i - 1, j, todo - 1)
            if i < m - 1 and grid[i + 1][j] != -1:
                utility(i + 1, j, todo - 1)
            if j > 0 and grid[i][j - 1] != -1:
                utility(i, j - 1, todo - 1)
            if j < n - 1 and grid[i][j + 1] != -1:
                utility(i, j + 1, todo - 1)
            grid[i][j] = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1:
                    obstacles += 1
                if grid[i][j] == 1:
                    x = i
                    y = j
                if grid[i][j] == 2:
                    hx = i
                    hy = j
        todo = m * n - 2 - obstacles

        utility(x, y, todo)
        print(ans)
        return ans


s = Solution()
s.uniquePathsIII([[1, 0, 0, 0],
                  [0, 0, 0, 0],
                  [2, 0, 0, -1]])

s.uniquePathsIII([[1, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 2]])