from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0 for i in range(n)] for j in range(m)]

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                cur = 0 if dungeon[i][j] >= 0 else - dungeon[i][j]
                next_cost = 0
                if i < m - 1 and j < n - 1:
                    next_cost = min(dp[i + 1][j], dp[i][j + 1])
                elif i < m - 1:
                    next_cost = dp[i + 1][j]
                elif j < n - 1:
                    next_cost = dp[i][j + 1]
                if next_cost > 0 and dungeon[i][j] > 0:
                    next_cost = max(next_cost - dungeon[i][j], 0)
        return dp[0][0] + 1