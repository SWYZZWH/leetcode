import heapq
import math
from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        M = 10 ** 9 + 7
        engineers = [(-efficiency[i], speed[i]) for i in range(n)]
        heapq.heapify(engineers)

        team = []
        res = 0
        cur_efficiency = math.inf
        cur_speed_sum = 0
        while engineers:
            e = heapq.heappop(engineers)
            # want to pop out the least speed engineer from team later
            heapq.heappush(team, (e[1], -e[0]))
            cur_efficiency = min(cur_efficiency, -e[0])
            cur_speed_sum += e[1]
            res = max(res, cur_efficiency * cur_speed_sum)
            if len(team) == k:
                # caculate the result
                e_fire = heapq.heappop(team)
                cur_speed_sum -= e_fire[0]

        return res % M
