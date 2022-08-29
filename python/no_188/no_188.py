import math
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0:
            return 0
        dp = [[0 for i in range(k + 1)] for j in range(len(prices))]

        ms = [math.inf for i in range(k + 1)]
        ret = 0
        for i in range(len(prices)):
            for j in range(0, k + 1):
                if i >= 1 and j >= 1:
                    dp[i][j] = max(dp[i - 1][j], prices[i] - ms[j - 1])
                    ret = max(ret, dp[i][j])
                ms[j] = min(ms[j], prices[i] - dp[i][j])

        return ret
