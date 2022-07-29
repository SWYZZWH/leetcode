# 1011. Capacity To Ship Packages Within D Days

# A conveyor belt has packages that must be shipped from one port to another within days days.
#
# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
#
# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

# Constraints:
#
# 1 <= days <= weights.length <= 5 * 104
# 1 <= weights[i] <= 500
import math
from typing import List


class Solution:
    # very difficult
    # excellent example for binary search
    # dp will exceed time limit
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        # dp = [[[math.inf for i in range(n)] for j in range(n)] for k in range(days)]
        # for k in range(days):
        #     if k == 0:
        #         for i in range(n):
        #             for j in range(i, n):
        #                 dp[k][i][j] = sum(weights[i: j])
        #     for i in range(0, n - k):
        #         for j in range(k, n):
        #             for l in range(0, k - 1):
        #                 for o in range(i, j):
        #                     for p in range(o, j):
        #                         dp[k][i][j] = min(max(dp[l][][], ))
        # return dp[days - 1][0][n]
        l, r = max(weights), sum(weights)
        while l < r:
            mid = (l + r) // 2
            cur = 0
            need = 1
            for weight in weights:
                if cur > mid:
                    need += 1
                    cur = 0
                cur += weight
            if need >= days:
                l = mid
            else:
                r = mid - 1

        return l
