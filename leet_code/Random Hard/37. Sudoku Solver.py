# https://leetcode.com/problems/sudoku-solver/

class Solution:
    def solveSudoku(self, board):
        dboard = [[1 for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                if i < 3:
                    if j < 3:
                        dboard[i][j] = 1
                    elif j < 6:
                        dboard[i][j] = 2
                    else:
                        dboard[i][j] = 3
                elif i < 6:
                    if j < 3:
                        dboard[i][j] = 4
                    elif j < 6:
                        dboard[i][j] = 5
                    else:
                        dboard[i][j] = 6
                else:
                    if j < 3:
                        dboard[i][j] = 7
                    elif j < 6:
                        dboard[i][j] = 8
                    else:
                        dboard[i][j] = 9

        from collections import defaultdict
        cdata = defaultdict(lambda: {'1', '2', '3', '4', '5', '6', '7', '8', '9'})
        rdata = defaultdict(lambda: {'1', '2', '3', '4', '5', '6', '7', '8', '9'})
        sbox = defaultdict(lambda: {'1', '2', '3', '4', '5', '6', '7', '8', '9'})

        empty = []

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    cdata[j].remove(board[i][j])
                    rdata[i].remove(board[i][j])
                    sbox[dboard[i][j]].remove(board[i][j])
                else:
                    empty.append((i, j))

        size = len(empty)
        t = 0
        not_found = True

        def solver(t):
            nonlocal cdata, rdata, sbox, dboard, board, not_found
            if t == size:
                not_found = False
                return
            i, j = empty[t]
            column = cdata[j]
            row = rdata[i]
            boxno = dboard[i][j]
            box = sbox[boxno]
            availabe_no = set.intersection(column, row, box)

            for each in availabe_no:
                if not not_found:
                    return
                cdata[j].remove(each)
                rdata[i].remove(each)
                sbox[boxno].remove(each)

                board[i][j] = each
                solver(t + 1)

                cdata[j].add(each)
                rdata[i].add(each)
                sbox[boxno].add(each)

        solver(0)
        for each in board:
            print(each)


s = Solution()
s.solveSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
               ["6", ".", ".", "1", "9", "5", ".", ".", "."],
               [".", "9", "8", ".", ".", ".", ".", "6", "."],
               ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
               ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
               ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
               [".", "6", ".", ".", ".", ".", "2", "8", "."],
               [".", ".", ".", "4", "1", "9", ".", ".", "5"],
               [".", ".", ".", ".", "8", ".", ".", "7", "9"]])