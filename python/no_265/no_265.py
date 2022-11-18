import heapq
from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        m, n = len(costs), len(costs[0])
        for i in range(1, m):
            cands = heapq.nsmallest(2, costs[i - 1])
            for j in range(n):
                if cands[0] == costs[i - 1][j]:
                    costs[i][j] += cands[1]
                else:
                    costs[i][j] += cands[0]

        return min(costs[-1])