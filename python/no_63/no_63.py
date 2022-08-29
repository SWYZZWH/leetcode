from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(m)]

        for i in reversed(range(0, m)):
            for j in reversed(range(0, n)):
                if obstacleGrid[i][j] == 1:
                    continue
                if i == m - 1 and j == n - 1:
                    dp[i][j] = 1
                    continue
                if i + 1 < m and obstacleGrid[i + 1][j] == 0:
                    dp[i][j] += dp[i + 1][j]
                if j + 1 < n and obstacleGrid[i][j + 1] == 0:
                    dp[i][j] += dp[i][j + 1]

        return dp[0][0]
