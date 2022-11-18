import math
from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n, total = len(nums), sum(nums)
        l, r = 0, total
        cur_min = math.inf
        res = -1
        for i in range(n - 1):
            l += nums[i]
            r -= nums[i]
            if abs(l // (i + 1) - r // (n - i - 1)) < cur_min:
                res = i
                cur_min = abs(l // (i + 1) - r // (n - i - 1))

        if total // n < cur_min:
            return n - 1

        return res


