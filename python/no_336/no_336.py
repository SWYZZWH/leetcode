import math
from typing import List


class Solution:
    # 5, 4, 3, 2, 1 -> False
    # 5, 3, 4 -> (3, 4) (i, j) i = 1, j = 2
    # 5, 3, 4, 5 -> i = 2, j = 3 -> (4, 5) -> find the answer
    # 5, 3, 4, 4 -> i = 2, j = 3 -> (4, 4) -> not an increasing pair
    # 5, 3, 4, 2 -> i = 2, j = 3 -> (4, 2) -> not an increasing pair
    # 5, 3, 4, 2, 5 -> (2, 5) 5 > 4 -> find the answer
    # 5, 3, 4, 2, 3 -> (2, 3) 3 <= 4 -> can't find the answer, replace with (2, 3)
    # 5, 3, 4, 2, 3, 4 -> (3, 4) 4 > 3 find the answer
    def increasingTriplet(self, nums: List[int]) -> bool:
        n, first, second = len(nums), math.inf, math.inf
        for i in range(n - 1):
            if nums[i] >= nums[i + 1]:
                if first < nums[i + 1] < second:
                    second = nums[i + 1]
                continue
            if second < nums[i + 1]:
                return True
            first = min(first, nums[i])
            second = min(second, nums[i + 1])

        return False

