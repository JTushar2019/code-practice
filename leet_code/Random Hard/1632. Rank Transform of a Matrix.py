# https://leetcode.com/problems/rank-transform-of-a-matrix/

class Solution:
    def matrixRankTransform(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        arr = [(i, j) for i in range(m) for j in range(n)]
        arr.sort(key=lambda x: matrix[x[0]][x[1]])
        from collections import defaultdict
        from math import inf
        rdata = defaultdict(lambda: (0, -inf))  # rank,number
        cdata = defaultdict(lambda: (0, -inf))  # rank,number
        newmat = [[0 for y in range(n)] for x in range(m)]
        i = 0
        while i < m * n:
            x = arr[i][0]
            y = arr[i][1]
            val = matrix[x][y]
            t = 0
            xdata = rdata[x][:]
            ydata = cdata[y][:]
            if val == xdata[1]:
                temp1 = xdata[0]
            else:
                temp1 = xdata[0] + 1
            if val == ydata[1]:
                temp2 = ydata[0]
            else:
                temp2 = ydata[0] + 1
            temp = max(temp2, temp1)
            newmat[x][y] = temp
            flag = True
            x1 = y1 = 0
            cdata[y] = (temp, val)
            rdata[x] = (temp, val)

            if val == xdata[1] and temp != temp1:
                flag = False
                x1 = x
                y1 = 0
                while matrix[x1][y1] != val:
                    y1 += 1
            if val == ydata[1] and temp != temp2:
                flag = False
                x1 = 0
                y1 = y
                while matrix[x1][y1] != val:
                    x1 += 1

            if not flag:
                while i > 0 and arr[i] != (x1, y1):
                    i -= 1
                continue
            i += 1
        print("*********")
        for each in newmat:
            print(each)
        return newmat


# s = Solution()
# mat = [[1, 2], [3, 4]]
# mat = [[7,7],[7,7]]
# mat = [[20, 21, -19], [-19, -19, 19], [-19, -47, 24], [-19, -19, 19]]
# mat = [[7,3,6],[1,4,5],[9,8,2]]
# mat = [[-42, 13, 40, 11, 30, 29, -16, -33, -6, -43, 0, 23, -50, 5],
#        [-32, -29, -6, 21, 8, 7, -50, 49, 28, 19, 34, -19, 48, 7],
#        [-6, 5, 48, -49, -46, 9, 44, -5, 10, 45, -28, -17, 10, 1],
#        [12, -21, -14, -39, 28, -9, 30, -31, 24, -9, 30, 37, -28, -49],
#        [-34, -31, 44, 7, 30, -11, -16, -21, 6, -3, 40, 31, -18, 1],
#        [44, -33, -18, 49, 0, 47, 2, 33, 16, -29, 46, -11, -28, -25],
#        [-6, 17, -40, -9, -2, 29, -16, -1, 34, 45, -32, -41, -10, -15],
#        [-4, -45, 6, -43, -16, 15, 30, 21, 32, -49, -46, 1, 16, 23],
#        [18, 25, 32, -41, 22, 33, 20, -17, -26, 13, 16, 43, -2, -11],
#        [16, -1, 38, 21, -28, -49, 46, -11, -48, 3, 38, -43, -48, 11],
#        [2, 9, -24, -49, -18, -31, 16, 31, 6, -3, -40, -33, 6, -47],
#        [-40, -37, 26, 21, -16, 3, 10, -19, 44, 11, 18, -3, 28, -17],
#        [14, -43, -32, 39, 2, 9, 44, -37, -38, -43, -8, 3, -26, 25],
#        [20, 15, 22, -35, -32, 35, 10, 29, 24, -29, -18, -19, -8, -9]]

# for each in mat:
#     print(each)
# print("************")
# s.matrixRankTransform(mat)