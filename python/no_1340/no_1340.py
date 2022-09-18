import functools
from typing import List


class Solution:
    # monotonic stack to build a graph with only O(N) edges
    # notice: we must climb up instead of going down (which we can prove the correctness of greedy algorithm)
    def maxJumps(self, arr: List[int], d: int) -> int:
        @functools.cache
        def dp(i: int):
            ret = 1
            for j in reversed(range(max(0, i - d), i)):
                if arr[j] < arr[i]:
                    ret = max(ret, 1 + dp(j))
                else:
                    break

            for j in range(i + 1, min(len(arr), i + d + 1)):
                if arr[j] < arr[i]:
                    ret = max(ret, 1 + dp(j))
                else:
                    break

            return ret

        m = 0
        for i in range(len(arr)):
            m = max(m, dp(i))

        return m
