from typing import List


class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        last = 0
        for i in range(len(nums)):
            if last + 1 < nums[i]:
                res += (last + 1 + min(nums[i] - 1, last + k)) * (min(nums[i] - last - 1, k)) // 2
                k -= nums[i] - last - 1
            if k <= 0:
                return res
            last = nums[i]
        if k:
            res += k * (last + 1) + k * (k - 1) // 2

        return res