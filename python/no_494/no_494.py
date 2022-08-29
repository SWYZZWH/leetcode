# 0 - 1 back pack, however the time complexity is too large, even after optimization
# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         zero_idx = sum(nums)
#         if target > zero_idx:
#             return 0
#
#         dp = [[0 for i in range(zero_idx * 2 + 1)] for j in range(len(nums))]
#
#         cur = set()
#         for i in range(len(nums)):
#             if i == 0:
#                 dp[0][nums[0] + zero_idx] += 1
#                 dp[0][zero_idx - nums[0]] += 1
#                 cur.add(nums[0] + zero_idx)
#                 cur.add(zero_idx - nums[0])
#                 continue
#             c_cur = set()
#             for idx in cur:
#                 if idx + nums[i] < len(dp[0]):
#                     dp[i][idx + nums[i]] += dp[i-1][idx]
#                     c_cur.add(idx + nums[i])
#                 if idx - nums[i] >= 0:
#                     dp[i][idx - nums[i]] += dp[i-1][idx]
#                     c_cur.add(idx - nums[i])
#             for c in c_cur:
#                 cur.add(c)
#
#         # print(dp)
#         return dp[-1][zero_idx + target]

# dfs and top-down dp is fast
from typing import List


class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums = sorted(nums, reverse=True) # opt 1
        total = sum(nums)

        suffix_sum = []
        prefix = 0
        for num in nums:
            suffix_sum.append(total - prefix)
            prefix += num

        # dfs and cut edges
        @functools.cache
        def dfs(idx: int, t: int) -> int:
            if idx == n:
                return 1 if t == 0 else 0

            if t > suffix_sum[idx] or t < -suffix_sum[idx]: # opt2 cut branch
                return 0

            ret = 0
            ret += dfs(idx + 1, t - nums[idx])
            ret += dfs(idx + 1, t + nums[idx])
            return ret

        return dfs(0, target)