import heapq
from typing import List


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        n = len(target)
        target = [-num for num in target]
        heapq.heapify(target)
        cur_sum = sum(target)
        while True:
            cur_max = heapq.heappop(target)
            if cur_max == -1 and len(target) == n - 1:
                return True
            cur_sum -= cur_max
            next_ele = cur_max - cur_sum
            if next_ele > -1:
                return False
            mul = next_ele // cur_sum
            next_ele -= mul * cur_sum
            if mul > 0 and next_ele == 0:
                next_ele += cur_sum
            if next_ele > -1:
                return False
            heapq.heappush(target, next_ele)
            cur_sum += next_ele
