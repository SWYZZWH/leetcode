import functools


class Solution:
    # simple fibnacci
    # def __init__(self):
    #     self.cache = {0: 0, 1: 1}

    @functools.cache
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# complete backpack solution WTF
class Solution:
    # complete backpack problem WTF
    def climbStairs(self, n: int) -> int:
        dp = [0 for i in range(n + 1)]
        dp[0] = 1

        for i in range(n + 1):
            for j in [1, 2]:
                if i >= j:
                    dp[i] += dp[i - j]

        return dp[n]
