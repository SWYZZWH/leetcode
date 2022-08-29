import math
from typing import List


class Solution:
    # simple dp
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0 for i in range(3)] for j in range(len(prices))]
        ms = [math.inf for i in range(3)]
        ret = 0
        for i in range(len(prices)):
            for j in range(0, 3):
                if i >= 1 and j >= 1:
                    dp[i][j] = max(dp[i - 1][j], prices[i] - ms[j - 1])
                ms[j] = min(ms[j], prices[i] - dp[i][j])
                ret = max(ret, dp[i][j])

        return ret
