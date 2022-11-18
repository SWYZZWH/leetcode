from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])

        def can_go_down(i: int, j: int) -> bool:
            if grid[i][j] == 1:
                return j + 1 < n and grid[i][j + 1] == 1
            else:
                return j - 1 >= 0 and grid[i][j - 1] == -1

        res = []
        for j in range(n):
            cur_j = j
            for i in range(m + 1):
                if i == m:
                    res.append(cur_j)
                    break
                if can_go_down(i, cur_j):
                    cur_j += 1 if grid[i][cur_j] == 1 else -1
                else:
                    res.append(-1)
                    break

        return res