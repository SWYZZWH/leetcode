class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7

        dp = [0 for i in range(target + 1)]
        dp[0] = 1
        for j in range(n):
            new_dp = [0 for i in range(target + 1)]
            for i in range(0, len(dp)):
                for l in range(1, k + 1):
                    if i + l < len(dp):
                        new_dp[i + l] += dp[i] % MOD
            dp = new_dp
        return dp[-1] % MOD