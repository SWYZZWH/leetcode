# class Solution:
#     # top-down dp
#     # bottom-up is also fine
#     # O(n^2)
#     def integerBreak(self, n: int) -> int:
#         dp = [1 for i in range(n + 1)]
#
#         for i in range(1, n + 1):
#             for j in range(1, i):
#                 dp[i] = max(dp[i], (i - j) * max(dp[j], j))
#
#         return dp[-1]


class Solution:
    # greedy, grep as many 3s possible, if the rest is 1, drop a 3 and multiple 4
    def integerBreak(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 1
        if n == 3:
            return 2

        ret = 1
        threes = n // 3
        if n % 3 == 1:
            threes -= 1
            ret *= 4
        elif n % 3 == 2:
            ret *= 2
        ret *= 3 ** threes

        return ret
