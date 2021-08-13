# https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/614/week-2-august-8th-august-14th/3888/

class Solution:
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        # flag = False
        # for i in range(n):
        #     if matrix[0][i] == 0:
        #         flag = True
        #         break
        # for i in range(m):
        #     nflag = False
        #     for j in range(n):
        #         if i+1 < m and matrix[i+1][j] == 0:
        #             nflag = True
        #         if matrix[i][j] == 0:
        #             if i+1 < m:
        #                 matrix[i+1][j] = 0
        #             if i > 0:
        #                 for t in range(i-1, -1, -1):
        #                     matrix[t][j] = 0
        #     if flag:
        #         for j in range(n):
        #             matrix[i][j] = 0
        #     flag = nflag

        row = column = False
        if 0 in matrix[0]:
            row = True
        for i in range(m):
            if matrix[i][0] == 0:
                column = True
                break

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row:
            for j in range(n):
                matrix[0][j] = 0
        if column:
            for j in range(m):
                matrix[j][0] = 0
        # return matrix
        for each in matrix:
            print(each)
        return matrix


s = Solution()
t = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
# t = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
# t = [[1,1,1],[1,0,1],[1,1,1]]
s.setZeroes(t)
