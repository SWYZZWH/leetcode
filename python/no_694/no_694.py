from typing import List


class Solution:
    # the key is how to distinguish one island with others
    # use 4 borders to define one island
    # compare all positions inside of borders to check if two islands are the same
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        s = set()

        directions = [
            ["l", 0, -1],
            ["r", 0, +1],
            ["u", +1, 0],
            ["d", -1, 0],
        ]

        def dfs(i: int, j: int, prefix: List[str]):
            for di in directions:
                r, c = i + di[1], j + di[2]
                if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                    grid[r][c] = 0
                    prefix.append(di[0])
                    dfs(r, c, prefix)
                    prefix.append("b")  # important !!!

        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                grid[i][j] = 0
                lst = []
                dfs(i, j, lst)
                h = "".join(lst)
                s.add(h)

        return len(s)
