import math
from typing import List


class Solution:
    # dp[i][0] = dp[i - 1][0], dp[i - 1][1] + prices[i] - fee
    # dp[i][1] = dp[i - 1][0] - prices[i], dp[i - 1][1]
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0, 0] for i in range(len(prices))]
        dp.append([0, -math.inf])

        ret = 0
        for i in range(len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][0] - prices[i], dp[i - 1][1])
            ret = max(ret, max(dp[i][0], dp[i][1]))

        return ret
