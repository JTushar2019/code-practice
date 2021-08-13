# https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/614/week-2-august-8th-august-14th/3888/

class Solution:
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        flag = False
        for i in range(n):
            if matrix[0][i] == 0:
                flag = True
                break
        for i in range(m):
            nflag = False
            for j in range(n):
                if i+1 < m and matrix[i+1][j] == 0:
                    nflag = True
                if matrix[i][j] == 0:
                    if i+1 < m:    
                        matrix[i+1][j] = 0
                    if i > 0:
                        for t in range(i-1, -1, -1):
                            matrix[t][j] = 0
            if flag:
                for j in range(n):
                    matrix[i][j] = 0
            flag = nflag

        for each in matrix:
            print(each)
        return matrix


s = Solution()
t = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
# t = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
# t = [[1,1,1],[1,0,1],[1,1,1]]
s.setZeroes(t)
