class Solution:
    # probability dp
    def knightProbability(self, n: int, k: int, r: int, c: int) -> float:
        moves = [
            [-1, -2],
            [-2, -1],
            [1, 2],
            [2, 1],
            [-1, 2],
            [-2, 1],
            [1, -2],
            [2, -1],
        ]
        error = 10 ** (-9)

        board = [[.0 for i in range(n)] for j in range(n)]
        board[r][c] = 1.
        for l in range(k):
            tmp_board = [[.0 for i in range(n)] for j in range(n)]
            for i in range(n):
                for j in range(n):
                    if abs(board[i][j]) < error:
                        continue
                    for m in moves:
                        new_r, new_c = i + m[0], j + m[1]
                        if 0 <= new_r < n and 0 <= new_c < n:
                            tmp_board[new_r][new_c] += board[i][j] * 0.125
            board = tmp_board

        return sum([sum(board[i]) for i in range(n)])