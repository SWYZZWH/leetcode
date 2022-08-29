import math


class Solution:
    # edit distance
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp = [[math.inf for i in range(n + 1)] for j in range(m + 1)]

        for i in range(0, m + 1):
            dp[i][0] = i

        for j in range(0, n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1, dp[i][j - 1] + 1)
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])

        return dp[-1][-1]

    # Longest common subsequence
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
                dp[i][j] = max(dp[i][j], dp[i][j - 1], dp[i - 1][j])

        return m - dp[-1][-1] + n - dp[-1][-1]