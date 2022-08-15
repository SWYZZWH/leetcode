import collections
from typing import List


class Solution:
    # two pass: from left to right & from right to left find the max
    # one pass: monotonic stack, we need 3 pillars : right, mid, left
    # use two pointers to reach O(n) & O(1):
    def trap(self, height: List[int]) -> int:
        stk = collections.deque()
        ret = 0
        for i, h in enumerate(height):
            # check two bars before
            while stk and stk[-1][1] <= h:
                idx, h0 = stk.pop()
                if not stk:
                    break
                ret += (i - stk[-1][0] - 1) * (min(h, stk[-1][1]) - h0)
            stk.append((i, h))
        return ret
