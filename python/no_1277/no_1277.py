from typing import List


class Solution:
    # if matrix[i][j] == 0 - > 0
    # dp[i][j] -> maximum size of square with the bottom-right corner at (i, j)
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    continue
                dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j + 1], dp[i][j]) + 1
                res += dp[i + 1][j + 1]

        return res

# class Solution:
#     # if matrix[i][j] == 0 - > 0
#     # dp[i][j] -> maximum size of square with the bottom-right corner at (i, j)
#     def countSquares(self, matrix: List[List[int]]) -> int:
#         res = 0
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] != 0 and i > 0 and j > 0:
#                     matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
#                 res += matrix[i][j]
#
#         return res