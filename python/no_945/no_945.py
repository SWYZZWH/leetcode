from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        last = nums[0] - 1
        res = 0
        for i in range(n):
            if nums[i] < last + 1:
                res += last + 1 - nums[i]
                last += 1
            else:
                last = nums[i]

        return res

