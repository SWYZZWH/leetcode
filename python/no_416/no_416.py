from typing import List


# yet another 0-1 backpack
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = total // 2
        if total != target * 2:
            return False

        dp = [False for j in range(target + 1)]
        dp[0] = True
        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = dp[j] or dp[j - nums[i]]

        return dp[target]
