import collections
from typing import List


class Solution:
    # classic monotonic problem
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ret = [0 for i in range(n)]
        stk = collections.deque()

        for i, t in enumerate(temperatures):
            while stk and t > stk[-1][0]:
                _, j = stk.pop()
                ret[j] = i - j
            stk.append((t, i))

        return ret
