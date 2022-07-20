# 2104. Sum of Subarray Ranges
# You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.
#
# Return the sum of all subarray ranges of nums.
#
# A subarray is a contiguous non-empty sequence of elements within an array.

# Constraints:
#
# 1 <= nums.length <= 1000
# -109 <= nums[i] <= 109
import math

# class Solution:
#     # naive way: O(n^3)
#     # keep max and min: O(n^2)
#     def subArrayRanges(self, nums: List[int]) -> int:
#         ret = 0
#         for i, num in enumerate(nums):
#             maxNum = -math.inf
#             minNum = math.inf
#             for j in range(i, len(nums)):
#                 maxNum = max(maxNum, nums[j])
#                 minNum = min(minNum, nums[j])
#                 ret += maxNum - minNum
#
#         return ret

# math O(n) solution is elegant, just like what we do in no_907
# we calculate the frequency map of which key is minimum value

# res = sum(A[i] * f(i))
# where f(i) is the number of subarrays,
# in which A[i] is the minimum.
# To get f(i), we need to find out:
# left[i], the length of strict bigger numbers on the left of A[i],
# right[i], the length of bigger numbers on the right of A[i].
# Then,
# left[i] + 1 equals to
# the number of subarray ending with A[i],
# and A[i] is single minimum.
#
# right[i] + 1 equals to
# the number of subarray starting with A[i],
# and A[i] is the first minimum.
#
# Finally f(i) = (left[i] + 1) * (right[i] + 1)
# to achieve O(N), use two increasing stacks
from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        return self.maxSubArraySum(nums) - self.minSubArraySum(nums)

    def minSubArraySum(self, nums: List[int]) -> int:
        return self.caculateSubArraySum(nums, True)

    def maxSubArraySum(self, nums: List[int]) -> int:
        return self.caculateSubArraySum(nums, False)

    def caculateSubArraySum(self, nums: List[int], getMin: bool):
        ret = 0
        stkLeft, stkRight = [], []
        leftRange, rightRange = [0] * len(nums), [0] * len(nums)

        for i, num in enumerate(nums):
            while len(stkLeft) != 0 and (getMin and num < stkLeft[-1][0] or not getMin and num > stkLeft[-1][0]):
                rightRange[stkLeft[-1][1]] = i - stkLeft[-1][1]
                stkLeft = stkLeft[:-1]
            stkLeft.append([num, i])
        while len(stkLeft) != 0:
            rightRange[stkLeft[-1][1]] = len(nums) - stkLeft[-1][1]
            stkLeft = stkLeft[:-1]

        for i in reversed(range(len(nums))):
            num = nums[i]
            while len(stkRight) != 0 and (getMin and num <= stkRight[-1][0] or not getMin and num >= stkRight[-1][0]):
                leftRange[stkRight[-1][1]] = stkRight[-1][1] - i
                stkRight = stkRight[:-1]
            stkRight.append([num, i])
        while len(stkRight) != 0:
            leftRange[stkRight[-1][1]] = stkRight[-1][1] + 1
            stkRight = stkRight[:-1]


        for i in range(len(nums)):
            ret += leftRange[i] * rightRange[i] * nums[i]

        return ret
