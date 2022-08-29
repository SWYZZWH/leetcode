class Solution:
    # for index i in s, there will be two choices
    # if s[i] == t[j], then we add the dp[i][j] with dp[i - 1][j - 1]
    # we can also choose not to use s[i], in that case, we add the dp[i][j] with the dp[i - 1][j]
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        dp = [0 for j in range(n + 1)]
        dp[0] = 1

        for i in range(1, m + 1):
            for j in reversed(range(1, n + 1)):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[-1]