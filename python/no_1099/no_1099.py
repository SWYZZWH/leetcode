import math
from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        cur_max = -math.inf
        while i < j:
            if nums[i] + nums[j] < k:
                cur_max = max(cur_max, nums[i] + nums[j])
                i += 1
            else:
                j -= 1

        return -1 if cur_max == -math.inf else cur_max