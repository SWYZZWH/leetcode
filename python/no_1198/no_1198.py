import heapq
import math
from typing import List


class Solution:
    # k pointers, use heap
    # best will be O(MN), similar to this, but we can only focus on current max elements
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        h = [(mat[i][0], i, 0) for i in range(m)]
        cur_cnt = 0
        cur_min = -math.inf
        heapq.heapify(h)
        while h:
            e = heapq.heappop(h)
            if mat[e[1]][e[2]] != cur_min:
                cur_cnt = 1
                cur_min = mat[e[1]][e[2]]
            else:
                cur_cnt += 1
                if cur_cnt == m:
                    return cur_min
            if e[2] + 1 < n:
                heapq.heappush(h, (mat[e[1]][e[2] + 1], e[1], e[2] + 1))

        return -1