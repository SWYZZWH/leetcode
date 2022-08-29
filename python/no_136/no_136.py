from typing import List


class Solution:
    # exlusive or
    def singleNumber(self, nums: List[int]) -> int:
        ret = nums[0]
        for i in range(1, len(nums)):
            ret ^= nums[i]

        return ret
