import collections
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = collections.Counter(nums)
        ret = [0, 0]
        for k, v in c.items():
            if v == 2:
                ret[0] = k

        for i in range(1, len(nums) + 1):
            if i not in c:
                ret[1] = i

        return ret