import math
from typing import List


class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        min_idx, min_val = -1, math.inf
        max_idx, max_val = -1, -math.inf
        for i in range(n):
            if nums[i] < min_val:
                min_idx, min_val = i, nums[i]
            if nums[i] >= max_val:
                max_idx, max_val = i, nums[i]

        if min_val == max_val:
            return 0

        res = min_idx + n - 1 - max_idx
        if min_idx > max_idx:
            res -= 1

        return res
