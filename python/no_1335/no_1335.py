import functools
from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty):
            return -1

        n = len(jobDifficulty)

        @functools.cache
        def dp(idx: int, d: int, last_max: int) -> int:
            last_max = max(last_max, jobDifficulty[idx])
            if d == n - idx:
                return last_max + sum(jobDifficulty[idx + 1:])

            if d == 1:
                return max(last_max, max(jobDifficulty[idx:]))

            return min(dp(idx + 1, d - 1, 0) + last_max, dp(idx + 1, d, last_max))

        return dp(0, d, 0)
