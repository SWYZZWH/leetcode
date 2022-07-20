# 33. Search in Rotated Sorted Array

# There is an integer array nums sorted in ascending order (with distinct values).
#
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
#
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
#
# You must write an algorithm with O(log n) runtime complexity.
import bisect
from typing import List


class Solution:
    # binary search
    # in normal order, left < right
    # however in border, left > right
    # notice: the arr is possibly rotated!
    # two pass can merge in one pass
    def search(self, nums: List[int], target: int) -> int:
        # find the pivot k
        # 1 <= k < nums.length
        n = len(nums)
        if n == 1:
            return -1 if target != nums[0] else 0
        if target == nums[0]:
            return 0
        if nums[0] < nums[-1]:
            # no rotate
            idx = bisect.bisect_left(nums, target)
            return -1 if idx == 0 or idx == n or nums[idx] != target else idx
        baseline = nums[0]
        l, r = 1, n
        k = -1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[mid - 1]:
                k = mid
                break
            if nums[mid] < baseline:
                r = mid
            else:
                l = mid + 1

        if target == baseline:
            return 0
        elif target == nums[k]:
            return k
        elif target < baseline:
            idx = bisect.bisect_left(nums, target, k)
            if idx == k or idx == n or nums[idx] != target:
                return -1
            return idx
        else:
            idx = bisect.bisect_left(nums, target, 0, k)
            if idx == 0 or idx == k or nums[idx] != target:
                return -1
            return idx
