import collections
from typing import List


class Solution:
    # BFS + back-tracking
    # or DFS + back-tracking
    # A*
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        s_i, s_j = -1, -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "*":
                    s_i, s_j = i, j

        if s_i == -1 or s_j == -1:
            return -1

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        q = collections.deque([(s_i, s_j)])
        visited = set([(s_i, s_j)])

        def pos_valid(i: int, j: int) -> int:
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if grid[i][j] == "X":
                return False
            if (i, j) in visited:
                return False
            return True

        res = 0
        while q:
            tmp = collections.deque()
            while q:
                node = q.popleft()
                if grid[node[0]][node[1]] == "#":
                    return res
                for d in directions:
                    pos = node[0] + d[0], node[1] + d[1]
                    if pos_valid(pos[0], pos[1]):
                        visited.add(pos)
                        tmp.append(pos)
            q = tmp
            res += 1

        return -1
