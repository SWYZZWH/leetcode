# 1675. Minimize Deviation in Array
# You are given an array nums of n positive integers.
#
# You can perform two types of operations on any element of the array any number of times:
#
# If the element is even, divide it by 2.
# For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
# If the element is odd, multiply it by 2.
# For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
# The deviation of the array is the maximum difference between any two elements in the array.
#
# Return the minimum deviation the array can have after performing some number of operations.

# basic idea is multiply every element in nums if it's odd, remove duplicated and push all in a heap / treemap
# find the max and min in the heap, let max /= 2, then push in the heap, update the deviation
# if max == min, return 0
# if max is odd, then return
import heapq
import math
from typing import List


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        nums = list(set([-num * 2 if num % 2 != 0 else -num for num in nums]))
        minimum = -max(nums)
        heapq.heapify(nums)

        ret = math.inf
        while True:
            curMax = -heapq.heappop(nums)
            ret = min(ret, curMax - minimum)
            if ret == 0 or curMax % 2 != 0:
                break
            curMax //= 2
            if curMax < minimum:
                minimum = curMax
            heapq.heappush(nums, -curMax)

        return ret
