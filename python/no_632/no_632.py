# 632. Smallest Range Covering Elements from K Lists
# You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.
#
# We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.
# nums.length == k
# 1 <= k <= 3500
# 1 <= nums[i].length <= 50
# -105 <= nums[i][j] <= 105
# nums[i] is sorted in non-decreasing order.
import heapq
from typing import List


class Solution:
    # use a heap to be more efficient
    # greedy, move the smallest element every time
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        if len(nums) == 1:
            return [nums[0][0], nums[0][0]]
        candidates = [(num[0], i) for i, num in enumerate(nums)]
        maximum = max(candidates)[0]
        minimum = min(candidates)[0]
        idxs = [0 for i in range(len(nums))]
        heapq.heapify(candidates)

        ret = [maximum - minimum, minimum, maximum]
        while True:
            e = heapq.heappop(candidates)
            idxs[e[1]] += 1
            if idxs[e[1]] >= len(nums[e[1]]):
                break
            newElement = (nums[e[1]][idxs[e[1]]], e[1])
            maximum = max(newElement[0], maximum)
            heapq.heappush(candidates, newElement)
            if candidates.__len__() >= 0:
                minimum = candidates[0][0]
            if maximum - minimum < ret[0]:
                ret = [maximum - minimum, minimum, maximum]
        return ret[1:]
