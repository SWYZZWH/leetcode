# 410. Split Array Largest Sum

# Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.
#
# Write an algorithm to minimize the largest sum among these m subarrays.
from typing import List


class Solution:
    # exactly the same code like no_1011
    # binary search
    def splitArray(self, nums: List[int], m: int) -> int:
        l, r = max(nums), sum(nums)
        while l < r :
            mid = (l + r) // 2
            need = 1
            cur = 0
            for num in nums:
                if cur + num > mid:
                    need += 1
                    cur = 0
                cur += num
            if need > m:
                # need > m is unacceptable
                l = mid + 1
            else:
                # need == m, need < m is acceptable solution, if we let r = mid - 1, the optimized answer may be overlooked
                r = mid
        return l