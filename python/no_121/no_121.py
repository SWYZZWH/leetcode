from typing import List


class Solution:
    # one pass: from left to right, hold the cur price until we find the price is lower than the cur price, we update cur price
    # else we just calculate the max profit
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        cur = -1
        for price in prices:
            if cur == -1:
                cur = price
                continue

            if price >= cur:
                ret = max(price - cur, ret)
                continue

            cur = price

        return ret
