import math
from typing import List


# coin change is also complete backpack problem hhh
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf for i in range(amount + 1)]
        dp[0] = 0

        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                dp[j] = min(dp[j], dp[j - coins[i]] + 1)

        return -1 if dp[amount] == math.inf else dp[amount]

# top-down dp is always fastest and most elegant solution for backpack problem
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         @functools.cache
#         def dfs(t: int) -> int:
#             if t == 0:
#                 return 0
#             ret = math.inf
#             for coin in coins:
#                 if t >= coin:
#                     ret = min(ret, dfs(t - coin) + 1)
#             return ret
#
#         ret = dfs(amount)
#         return -1 if ret == math.inf else ret

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf for i in range(amount + 1)]
        dp[0] = 0

        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                dp[j] = min(dp[j], dp[j - coins[i]] + 1)

        return dp[-1] if dp[-1] != math.inf else -1