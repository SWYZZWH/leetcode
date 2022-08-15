import heapq
from typing import List


class Solution:
    # we can only choose the minimum positive number each time
    def minimumOperations(self, nums: List[int]) -> int:
        h = [num for num in nums if num != 0]
        if len(h) == 0:
            return 0
        heapq.heapify(h)

        ret = 0
        while len(h) != 0:
            m = heapq.heappop(h)
            ret += 1
            while len(h) != 0 and h[0] <= m:
                heapq.heappop(h)
            for i in range(len(h)):
                h[i] -= m
        return ret
