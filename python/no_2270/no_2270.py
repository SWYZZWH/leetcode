# 2270. Number of Ways to Split Array
# You are given a 0-indexed integer array nums of length n.
#
# nums contains a valid split at index i if the following are true:
#
# The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
# There is at least one element to the right of i. That is, 0 <= i < n - 1.
# Return the number of valid splits in nums.

# Constraints:
#
# 2 <= nums.length <= 105
# -105 <= nums[i] <= 105
from typing import List


class Solution:
    # must run in O(n) or O(nlogn)
    def waysToSplitArray(self, nums: List[int]) -> int:
        left, right, ret = 0, sum(nums), 0
        # ret = 1 if left >= right else 0
        for i in range(0, len(nums) - 1):
            left += nums[i]
            right -= nums[i]
            if left >= right:
                ret += 1
        return ret
