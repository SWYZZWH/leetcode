from typing import List


class Solution:
    # two pointers
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 1, 0
        while i < len(nums):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
            i += 1
        return j + 1
