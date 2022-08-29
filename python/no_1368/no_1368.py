import collections
from typing import List


class Solution:
    # greedy
    # BFS
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()

        def expand(i: int, j: int):
            ret = []
            if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited:
                return ret

            ret.append((i, j))
            visited.add((i, j))

            d = grid[i][j]
            if d == 1:
                ret += expand(i, j + 1)
            if d == 2:
                ret += expand(i, j - 1)
            if d == 3:
                ret += expand(i + 1, j)
            if d == 4:
                ret += expand(i - 1, j)

            return ret

        for i, j in expand(0, 0):
            q.append((i, j))

        cost = 0
        while q:
            tmp_q = collections.deque()
            while q:
                i, j = q.popleft()
                d = grid[i][j]
                if i == m - 1 and j == n - 1:
                    return cost

                for k in range(1, 5):
                    if d == k:
                        continue
                    if k == 1:
                        for ii, jj in expand(i, j + 1):
                            tmp_q.append((ii, jj))
                    if k == 2:
                        for ii, jj in expand(i, j - 1):
                            tmp_q.append((ii, jj))
                    if k == 3:
                        for ii, jj in expand(i + 1, j):
                            tmp_q.append((ii, jj))
                    if k == 4:
                        for ii, jj in expand(i - 1, j):
                            tmp_q.append((ii, jj))

            cost += 1
            q = tmp_q
