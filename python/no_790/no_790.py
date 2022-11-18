import functools


# Matrix Exponentiation
class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        @functools.cache
        def dfs(n: int, last: int) -> int:
            if n == 0:
                if last == 0:
                    return 1
                else:
                    return 0
            if n == 1:
                return 1

            if last == 0:
                return (dfs(n - 1, 0) + dfs(n - 2, 1) + dfs(n - 2, 2) + dfs(n - 2, 0)) % MOD
            if last == 1:
                return (dfs(n - 1, 2) + dfs(n - 1, 0)) % MOD
            if last == 2:
                return (dfs(n - 1, 1) + dfs(n - 1, 0)) % MOD

        return dfs(n, 0) % MOD