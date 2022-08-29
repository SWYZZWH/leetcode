import functools


class Solution:
    # what the fuck is Catalan number
    def numTrees(self, n: int) -> int:
        # number of different BST of size n
        sorted(reverse=True)
        dp = [0 for i in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(0, i):
                dp[i] += (max(dp[j], 1) * max(dp[i - j - 1], 1))

        return dp[n]