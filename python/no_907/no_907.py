# like no_2104, find the sum of minimum of each subarray
from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        return self.minSubArraySum(nums)

    def minSubArraySum(self, nums: List[int]) -> int:
        return self.caculateSubArraySum(nums, True)

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
            stkLeft.pop()

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
            ret += (leftRange[i] * rightRange[i] * nums[i]) % 1_000_000_007

        return ret % 1_000_000_007
