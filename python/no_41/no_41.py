# 41. First Missing Positive

# Given an unsorted integer array nums, return the smallest missing positive integer.
#
# You must implement an algorithm that runs in O(n) time and uses constant extra space.
from typing import List


class Solution:
    # put the number in the right place
    # another way is change the sign of num[i] if i show up, but we have to remove 0 and negative numbers first
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            if nums[i] <= 0 or nums[i] > n or nums[i] == i + 1:
                continue
            else:
                while 0 < nums[i] <= n and nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                    target = nums[i] - 1
                    nums[i], nums[target] = nums[target], nums[i]
        for i in range(0, n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
