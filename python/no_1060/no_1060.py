from typing import List


class Solution:
    # binary search
    # nums [4, 7, 9, 10]
    # minus nums[0], arr = [0, 3, 5, 6]
    # the index arr idx = [0, 1, 2, 3]
    # missing = arr - idx = [0, 2, 3 ,3]
    # we search k in missing, find the left most element, and plus the rest
    # The idea is to find the leftmost element such that the number of missing numbers until this element is less or equal to k.
    def missingElement(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            missing = nums[mid] - nums[0] - mid
            if missing < k:
                l = mid + 1  # before break loop, if the last step is update l, then in the last round, mid = l - 1, there is missing(l - 1) < k else, there is missing(r) >= k
            else:
                r = mid
        # missing(left - 1) < k <= missing(left)
        # k > 0, so the l won't be k
        # the nums[l] is the left most element, so nums[l] - 1 must be a missing number
        # then we just to add k - missing +
        return nums[l - 1] + k - (nums[l - 1] - nums[0] - (l - 1))
