# 1182. Shortest Distance to Target Color

# You are given an array colors, in which there are three colors: 1, 2 and 3.
#
# You are also given some queries. Each query consists of two integers i and c, return the shortest distance between the given index i and the target color c. If there is no solution return -1.

# Constraints:
#
# 1 <= colors.length <= 5*10^4
# 1 <= colors[i] <= 3
# 1 <= queries.length <= 5*10^4
# queries[i].length == 2
# 0 <= queries[i][0] < colors.length
# 1 <= queries[i][1] <= 3
import math
from typing import List


class Solution:
    # visit twice, from left to right, and from right to left, for every color:
    # the dist[i][j] (j for color index) = min(left[i][j], right[i][j])

    # also can be solved by binary search with higher complexity
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        n = len(colors)
        left, right = [[math.inf, math.inf, math.inf]] * n, [[math.inf, math.inf, math.inf]] * n
        # left, right = [], []
        curMin = [math.inf, math.inf, math.inf]
        for i in range(n):
            for j in range(3):
                if j != colors[i] - 1:
                    curMin[j] += 1
                else:
                    curMin[j] = 0
            left[i] = [curMin[0], curMin[1], curMin[2]]
        curMin = [math.inf, math.inf, math.inf]
        for i in reversed(range(n)):
            for j in range(3):
                if j != colors[i] -1:
                    curMin[j] += 1
                else:
                    curMin[j] = 0
            right[i] = [curMin[0], curMin[1], curMin[2]]

        ret = []
        for q in queries:
            dist = min(left[q[0]][q[1] - 1], right[q[0]][q[1] - 1])
            if dist > 1000000:
                ret.append(-1)
            else:
                ret.append(dist)
        return ret
