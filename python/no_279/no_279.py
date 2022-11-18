import math


# we can use 4 number theory
class Solution:
    def numSquares(self, n: int) -> float:
        square_nums = [i ** 2 for i in range(0, int(math.sqrt(n)) + 1)]
        dp = [math.inf for i in range(n + 1)]
        dp[0] = 0
        for i in range(1, len(dp)):
            for j in square_nums:
                if i < j:
                    break
                dp[i] = min(dp[i], dp[i - j] + 1)

        return dp[n]
