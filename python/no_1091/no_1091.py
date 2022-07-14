# 1091. Shortest Path in Binary Matrix
# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.
#
# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
#
# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

# Constraints:
#
# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1

from collections import deque
from typing import List


class Solution:
    # classic BFS with visited grid
    def visit(self, i, j, m, n, grid) -> bool:
        if m > i >= 0 and n > j >= 0 and grid[i][j] == 0:
            grid[i][j] = 1
            return True
        return False

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][0] != 0 or grid[m - 1][n - 1] != 0:
            return -1

        # i, j, level
        q = deque()
        q.append([0, 0, 1])
        while q.__len__() != 0:
            tmpQ = deque()
            while q.__len__() != 0:
                e = q.pop()
                i, j, level = e[0], e[1], e[2]
                if i == m - 1 and j == n - 1:
                    return level
                for ii, jj in [(i - 1, j - 1), (i, j - 1), (i + 1, j - 1), (i - 1, j), (i + 1, j), (i - 1, j + 1), (i, j + 1), (i + 1, j + 1)]:
                    if self.visit(ii, jj, m, n, grid):
                        tmpQ.append([ii, jj, level + 1])
                # self.visit(i - 1, j - 1, m, n, grid)
                # self.visit(i, j - 1, m, n, grid)
                # self.visit(i + 1, j - 1, m, n, grid)
                # self.visit(i - 1, j, m, n, grid)
                # self.visit(i + 1, j, m, n, grid)
                # self.visit(i - 1, j + 1, m, n, grid)
                # self.visit(i, j + 1, m, n, grid)
                # self.visit(i + 1, j + 1, m, n, grid)
            q = tmpQ
        return -1
