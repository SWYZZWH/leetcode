from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ret = 1
        cur_len = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur_len += 1
                ret = max(ret, cur_len)
            else:
                cur_len = 1

        return ret
