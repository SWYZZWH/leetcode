import collections
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        c = collections.Counter(tasks)
        ret = 0
        for k, v in c.items():
            if v == 1:
                return -1
            if v % 3 == 0:
                ret += v // 3
            else:
                ret += v // 3 + 1

        return ret
