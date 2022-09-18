import collections
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = collections.deque()
        ret = 0
        for i, h in enumerate(heights):
            idx = i
            while stk and stk[-1][0] >= h:
                hh, idx = stk.pop()
                ret = max(ret, hh * (i - idx))
            stk.append((h, idx))

        while stk:
            h, i = stk.pop()
            ret = max(ret, h * (len(heights) - i))

        return ret
