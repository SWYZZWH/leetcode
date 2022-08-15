from typing import List


class Solution:
    # simple DFS/BFS
    # union find is also fine
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        ret = 0

        def dfs(i: int, j: int):
            if i < 0 or i >= m or j < 0 or j >= n:
                return

            if grid[i][j] != '1':
                return

            grid[i][j] = '2'
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ret += 1

        return ret