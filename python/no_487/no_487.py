from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if 0 not in nums:
            return len(nums)
        cur_max = 0
        left = 0
        cur = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cur += 1
                continue
            cur_max = max(cur_max, cur + left + 1)
            left = cur
            cur = 0
        if cur:
            cur_max = max(cur_max, cur + left + 1)

        return cur_max