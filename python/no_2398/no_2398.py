from collections import deque
from typing import List


class Solution:
    # sliding window
    # O(N), O(N)
    # typical template for sliding window & monotonic queue
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        # monotonic queue for getting the maximum of any subarray in O(1)
        q = deque()
        i = cur_sum = 0
        for j in range(n):
            # expand
            while q and q[-1][0] < chargeTimes[j]:
                q.pop()
            q.append((chargeTimes[j], j))
            cur_sum += runningCosts[j]

            if q[0][0] + (j - i + 1) * cur_sum > budget:
                if i >= q[0][1]:
                    q.popleft()
                cur_sum -= runningCosts[i]
                i += 1

        return n - i