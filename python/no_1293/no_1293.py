import collections
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        q = collections.deque([(0, 0, 0, 0)])
        visited = {}
        while q:
            node = q.popleft()
            if node[2] < 0:
                continue
            if node[0] == m - 1 and node[1] == n - 1:
                return node[3]
            if node[0] < 0 or node[0] >= m or node[1] < 0 or node[1] >= n:
                continue
            if (node[0], node[1]) in visited and node[2] + grid[node[0]][node[1]] >= visited[(node[0], node[1])]:
                continue
            if node[2] + grid[node[0]][node[1]] > k:
                continue
            visited[(node[0], node[1])] = node[2] + grid[node[0]][node[1]]
            q.append((node[0] + 1, node[1], visited[(node[0], node[1])], node[3] + 1))
            q.append((node[0], node[1] + 1, visited[(node[0], node[1])], node[3] + 1))
            q.append((node[0] - 1, node[1], visited[(node[0], node[1])], node[3] + 1))
            q.append((node[0], node[1] - 1, visited[(node[0], node[1])], node[3] + 1))

        return -1
