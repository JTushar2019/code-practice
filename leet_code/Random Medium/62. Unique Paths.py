# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m, n):
        # def utility(i, j):
        #     nonlocal m, n
        #     if i == m - 1 and j == n - 1:
        #         return 0
        #     elif i == m - 1:
        #         return utility(i, j + 1)
        #     elif j == n - 1:
        #         return utility(i + 1, j)
        #     elif i < m or j < n:
        #         return utility(i + 1, j) + utility(i, j + 1)
        #
        # return utility(0, 0)
        matrix = [[0 for i in range(n)] for i in range(m)]

        for i in range(m):
            matrix[i][0] = 1
        for i in range(n):
            matrix[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

        return matrix[m - 1][n - 1]