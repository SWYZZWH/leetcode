import math
from typing import List


class Solution:
    # sort points by x_start
    # maintains a right border (x_end)
    # if start point of next point is smaller than x_end, continue
    # else, ret += 1 and update right border as the x_end of this new point
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], x[1]))
        # print(points)
        right = -math.inf
        ret = 0
        for p in points:
            if p[0] > right:
                ret += 1
                right = p[1]
            # greedy
            if p[1] < right:
                right = p[1]
        return ret
