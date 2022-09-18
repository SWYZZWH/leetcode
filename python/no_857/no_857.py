import bisect
import heapq
import math
from typing import List

import sortedcontainers
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        efficiency = [(wage[i] / quality[i]) for i in range(n)]

        h = [(efficiency[i], quality[i]) for i in range(n)]
        heapq.heapify(h)

        # print(h)
        team = []
        res = math.inf
        cur_eff = 0
        cur_sum = 0
        while h:
            e = heapq.heappop(h)
            heapq.heappush(team, (-e[1], e[0]))
            # print(team)
            cur_eff = max(cur_eff, e[0])
            cur_sum += e[1]
            if len(team) == k:
                res = min(res, cur_sum * cur_eff)
                e_fire = heapq.heappop(team)
                cur_sum -= -e_fire[0]
            bisect.bisect_left()
        sortedcontainers.SortedDict()
        return res
