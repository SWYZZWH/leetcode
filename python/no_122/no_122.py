from typing import List


class Solution:
    # find each increasing interval
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                ret += prices[i + 1] - prices[i]

        return ret
