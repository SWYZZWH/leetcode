import bisect
from typing import List


class Solution:
    # O(n^2) solution
    # may be O(n log n) is possible
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for i in range(len(nums))]

        ret = 1
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] <= nums[j]:
                    continue
                dp[i] = max(dp[i], dp[j] + 1)
            ret = max(ret, dp[i])
        return ret

    # beautiful solution: Try to build a sequence, Override and Binary Search
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = []

        for num in nums:
            if len(arr) == 0 or num > arr[-1]:
                arr.append(num)
                continue
            idx = bisect.bisect_left(arr, num)
            arr[idx] = num

        return len(arr)
