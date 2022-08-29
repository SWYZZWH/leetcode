import functools
from typing import List


# simple, clean and fast
class Solution:

    def combinationSum4(self, nums: List[int], target: int) -> int:
        @functools.cache
        def dfs(t: int) -> int:
            if t == 0:
                return 1
            ret = 0
            for num in nums:
                if t >= num:
                    ret += dfs(t - num)
            return ret

        return dfs(target)


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # minor optimization
        # nums.sort()
        dp = [0 for i in range(target+1)]
        dp[0] = 1

        # loop sequence can be reversed to calculate combinations differently
        for comb_sum in range(target+1):
            for num in nums:
                if comb_sum - num >= 0:
                    dp[comb_sum] += dp[comb_sum-num]
                # minor optimization, early stopping.
                # else:
                #    break
        return dp[target]
