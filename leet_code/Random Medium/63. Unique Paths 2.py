# https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, matrix):

        m = len(matrix)
        n = len(matrix[0])
        if matrix[0][0]:
            return 0

        for i in range(m):
            if matrix[i][0] == 1:
                for j in range(i, m):
                    matrix[j][0] = 0
                break
            matrix[i][0] = 1
        for i in range(1, n):
            if matrix[0][i] == 1:
                for j in range(i, n):
                    matrix[0][j] = 0
                break
            matrix[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
                else:
                    matrix[i][j] = 0

        for each in matrix:
            print(each)
        return matrix[m - 1][n - 1]


s = Solution()
s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])