class Solution:
    # top-down dp is easy to write
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        if n == 1:
            return 1

        dp = [[0 for i in range(n)] for j in range(n)]

        for l in range(0, n):
            for i in range(0, n - l):
                j = i + l
                if i == j:
                    dp[i][j] = 1
                    continue
                if s[i] == s[j]:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j - 1] + 2 if j - 1 >= i + 1 else 2)
                dp[i][j] = max(dp[i][j], dp[i + 1][j], dp[i][j - 1])

        return dp[0][-1]