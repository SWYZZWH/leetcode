import heapq
from typing import List


# this problem can be solved by counting sort!!
class Solution:
    # mock this procedure with heap
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if first != second:
                heapq.heappush(stones, first - second)

        return -stones[0] if stones else 0
