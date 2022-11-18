import functools
from typing import List


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10 ** 9 + 7
        m, n = len(pizza), len(pizza[0])
        prefix_sum = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                prefix_sum[i][j] = prefix_sum[i][j + 1] + prefix_sum[i + 1][j] - prefix_sum[i + 1][j + 1] + (1 if pizza[i][j] == "A" else 0)

        @functools.cache
        def dfs(r: int, c: int, k: int) -> int:
            if k == 0:
                return 1

            methods = 0
            for i in range(r + 1, m):
                if prefix_sum[i][c] == 0:
                    break
                if prefix_sum[i][c] == prefix_sum[r][c]:
                    continue
                methods += dfs(i, c, k - 1)
                methods %= MOD

            for j in range(c + 1, n):
                if prefix_sum[r][j] == 0:
                    break
                if prefix_sum[r][j] == prefix_sum[r][c]:
                    continue
                methods += dfs(r, j, k - 1)
                methods %= MOD

            return methods

        return dfs(0, 0, k - 1)
