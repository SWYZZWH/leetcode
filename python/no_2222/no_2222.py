# dp
# valid for any required number of buildings including 3
# state machine
class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        dp = [[1, 1], [0, 0], [0, 0], [0, 0]]
        for i in range(n):
            for j in reversed(range(1, 4)):
                if s[i] == '0':
                    dp[j][0] += dp[j - 1][1]
                else:
                    dp[j][1] += dp[j - 1][0]
        return sum(dp[-1])