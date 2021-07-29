# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/612/week-5-july-29th-july-31st/3831/
# https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat):
        from collections import deque
        q = deque()
        l = len(mat)
        b = len(mat[0])
        visited = {}
        for i in range(l):
            for j in range(b):
                if mat[i][j] == 0:
                    q.append((i, j))
                    visited[(i, j)] = True
                else:
                    mat[i][j] = 100000

        while len(q):
            node = q.popleft()
            i, j = node
            val = mat[i][j]
            if 0 < i:
                mat[i - 1][j] = min(mat[i - 1][j], val + 1)
                if (i - 1, j) not in visited:
                    visited[(i - 1, j)] = True
                    q.append((i - 1, j))
            if i < l - 1:
                mat[i + 1][j] = min(mat[i + 1][j], val + 1)
                if (i + 1, j) not in visited:
                    visited[(i + 1, j)] = True
                    q.append((i + 1, j))
            if 0 < j:
                mat[i][j - 1] = min(mat[i][j - 1], val + 1)
                if (i, j - 1) not in visited:
                    visited[(i, j - 1)] = True
                    q.append((i, j - 1))
            if j < b - 1:
                mat[i][j + 1] = min(mat[i][j + 1], val + 1)
                if (i, j + 1) not in visited:
                    visited[(i, j + 1)] = True
                    q.append((i, j + 1))

        for each in mat:
            print(each)
        return mat


s = Solution()
# mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
# mat = [[0,0,0],[0,1,0],[0,0,0]]
mat = [[0, 1, 1, 1, 1, 0]]
s.updateMatrix(mat)