# A peak element is an element that is strictly greater than its neighbors.
#
#  Given a 0-indexed integer array nums, find a peak element, and return its
# index. If the array contains multiple peaks, return the index to any of the peaks.
#
#
#  You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is
# always considered to be strictly greater than a neighbor that is outside the
# array.
#
#  You must write an algorithm that runs in O(log n) time.
#
#
#  Example 1:
#
#
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index
# number 2.
#
#  Example 2:
#
#
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak
# element is 2, or index number 5 where the peak element is 6.
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 1000
#  -2³¹ <= nums[i] <= 2³¹ - 1
#  nums[i] != nums[i + 1] for all valid i.
#
#
#  Related Topics Array Binary Search 👍 6722 👎 3884


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


# it's hard to come across this can be solved by binary search without any hints
class Solution:
    def rec(self, nums: List[int], l: int, r: int) -> int:
        if r - l == 1:
            return l

        if r - l == 2:
            if nums[l] > nums[l + 1]:
                return l
            return l + 1

        mid = (l + r) // 2
        if nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid]:
            return mid
        if nums[mid - 1] > nums[mid]:
            return self.rec(nums, l, mid)
        return self.rec(nums, mid + 1, r)

    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        return self.rec(nums, l, r)

# leetcode submit region end(Prohibit modification and deletion)
