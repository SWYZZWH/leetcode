# yet another dp problem
import sortedcontainers


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = 1

        sd = sortedcontainers.SortedDict()
        sd.update()
        sd.setdefault()
        sd.peekitem()

        for i in range(m):
            for j in range(n):
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
                if i > 0:
                    dp[i][j] += dp[i - 1][j]

        return dp[m - 1][n - 1]
