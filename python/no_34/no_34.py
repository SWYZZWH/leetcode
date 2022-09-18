from bisect import bisect
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        idx1 = bisect.bisect_left(nums, target)
        idx2 = bisect.bisect_right(nums, target)
        return [idx1, idx2 - 1] if idx1 != len(nums) and target == nums[idx1] else [-1, -1]


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bisect_right(nums: List[int], target: int):
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid
                else:
                    l = mid + 1
            return l

        def bisect_left(nums: List[int], target: int):
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] >= target:
                    r = mid
                else:
                    l = mid + 1
            return l

        idx1 = bisect_left(nums, target)
        idx2 = bisect_right(nums, target)
        return [idx1, idx2 - 1] if idx1 != len(nums) and target == nums[idx1] else [-1, -1]
