import math
from typing import List


class Solution:
    # dp[i][k][l] i means day i, k means max limit of transactions, l means stocks hold in hands
    # dp[i][k][0] = dp[i - 1][k][0], dp[i - 1][k][1] + prices[i] # sell on day i
    # dp[i][k][1] = dp[i - 1][k][1], dp[i - 2][k + 1][0] - prices[i - 1] # buy on day i - 1
    # one thing to notice that we can use dp[i-2] directly because dp[i - 1][k][0] is just the same as dp[i - 2][k][0] if dp[i - 2][k][1] is not considered (which needs to be sold on day i - 1)

    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0 for i in range(2)] for j in range(len(prices))]
        dp.append([0, 0])  # prepare -2
        dp.append([0, -math.inf])  # prepare -1

        ret = 0  # i - 1 day max profit
        for i in range(len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
            ret = max(ret, max(dp[i][0], dp[i][1]))

        return ret
