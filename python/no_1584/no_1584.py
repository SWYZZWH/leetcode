import heapq
from typing import List


class Solution:
    # MST
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = [(0, 0)]

        visited = set()
        ret = 0
        while dist:
            tp = heapq.heappop(dist)
            if tp[1] in visited:
                continue
            visited.add(tp[1])

            ret += tp[0]

            for i in range(n):
                if i in visited:
                    continue
                d = abs(points[tp[1]][0] - points[i][0]) + \
                    abs(points[tp[1]][1] - points[i][1])
                heapq.heappush(dist, (d, i))

        return ret
