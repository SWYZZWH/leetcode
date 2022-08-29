from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = len(nums) - 1
        for i in range(len(nums)):
            while idx > 0 and nums[idx] == val:
                idx -= 1
            if i >= idx:
                return i if nums[i] == val else i + 1
            if nums[i] == val:
                nums[i], nums[idx] = nums[idx], nums[i]

        return idx
