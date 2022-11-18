import math
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = matrix[0].copy()

        for i in range(1, m):
            tmp = [math.inf for i in range(m)]
            for j in range(n):
                if j > 0:
                    tmp[j] = min(tmp[j], dp[j - 1] + matrix[i][j])
                if j < n - 1:
                    tmp[j] = min(tmp[j], dp[j + 1] + matrix[i][j])
                tmp[j] = min(tmp[j], dp[j] + matrix[i][j])
            dp = tmp

        return min(dp)