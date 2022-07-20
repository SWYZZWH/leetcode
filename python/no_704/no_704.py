# 704. Binary Search
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.
import random
from typing import List


class Solution:
    # standard implement
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)
        while i < j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid
        return target if i == j and nums[i] == target else -1


    def binary_sort(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)
        while i < j:
            idx = self.quickSelect(nums, i, j)
            if nums[idx] == target:
                return idx
            elif nums[idx] < target:
                i = idx + 1
            else:
                j = idx

        if i == j:
            return i
        else:
            return -1

    def quickSelect(self, nums: List[int], begin: int, end: int) -> int:
        idx = random.randint(begin, end - 1)
        nums[idx], nums[begin] = nums[begin], nums[idx]
        k = begin + 1
        l = begin
        while k < end:
            if nums[0] >= nums[k]:
                l += 1
                nums[k], nums[l] = nums[l], nums[k]
            k += 1
        nums[0], nums[l] = nums[l], nums[0]
        return l
