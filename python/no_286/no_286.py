import collections
from typing import List


class Solution:

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # BFS
        # BFS and DFS can start with multiple roots
        # for most cases, BFS only needs single while loop
        m, n = len(rooms), len(rooms[0])
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j, 0))

        def search_around(i, j, dist):
            if i < 0 or i >= m or j < 0 or j >= n:
                return

            if rooms[i][j] == -1 or dist >= rooms[i][j]:
                return

            rooms[i][j] = dist
            q.append((i, j, dist))

        while q:
            i, j, dist = q.popleft()
            search_around(i - 1, j, dist + 1)
            search_around(i + 1, j, dist + 1)
            search_around(i, j - 1, dist + 1)
            search_around(i, j + 1, dist + 1)
