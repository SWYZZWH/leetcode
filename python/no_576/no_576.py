class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7
        board = [[0 for j in range(n)] for i in range(m)]
        board[startRow][startColumn] = 1
        res = 0

        def cnt_ways(board) -> int:
            res = 0
            for i in range(m):
                for j in range(n):
                    if i + 1 >= m:
                        res += board[i][j]
                    if i - 1 < 0:
                        res += board[i][j]
                    if j + 1 >= n:
                        res += board[i][j]
                    if j - 1 < 0:
                        res += board[i][j]
            return res

        for i in range(maxMove):
            res += cnt_ways(board) % MOD
            new_board = [[0 for j in range(n)] for i in range(m)]
            for i in range(m):
                for j in range(n):
                    if board[i][j] == 0:
                        continue
                    if i + 1 < m:
                        new_board[i + 1][j] += board[i][j]
                    if i - 1 >= 0:
                        new_board[i - 1][j] += board[i][j]
                    if j + 1 < n:
                        new_board[i][j + 1] += board[i][j]
                    if j - 1 >= 0:
                        new_board[i][j - 1] += board[i][j]
            board = new_board

        return res % MOD
