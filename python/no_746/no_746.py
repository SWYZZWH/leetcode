# dp problem
# recurrence relation is
#  dp[n] = min(dp[n - 1] + nums[n - 1], dp[n - 2] + nums[n - 2])
#  initial states are:
#   dp[0] = 0 & dp[1] = 0
import math
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [math.inf for i in range(len(cost) + 1)]
        dp[0], dp[1] = 0, 0

        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[-1]
