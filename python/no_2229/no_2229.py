import math
from typing import List


class Solution:
    # no duplicated element
    # maintain the maximum and minimum
    # check len(nums) == maximum - minimum + 1
    def isConsecutive(self, nums: List[int]) -> bool:
        if len(nums) == 0 or len(nums) == 1:
            return True

        visited = set()
        mini, maxi = math.inf, - math.inf
        for num in nums:
            if num in visited:
                return False
            visited.add(num)
            if num < mini:
                mini = num
            if num > maxi:
                maxi = num

        return len(nums) == maxi - mini + 1

