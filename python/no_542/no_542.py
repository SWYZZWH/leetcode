import math
from typing import List


class Solution:
    # dp
    # main problem is: we can only decide the dist after we know all 4 dimensional neighbors
    # so we do dp twice
    # from left top to right bottom
    # from right bottom to left top
    # and dp is the only way to get O(1) space complexity
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ret = [[math.inf for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                if ret[i][j] == 0 or mat[i][j] == 0:
                    ret[i][j] = 0
                    continue
                if i > 0:
                    ret[i][j] = min(ret[i][j], ret[i - 1][j] + 1)
                if j > 0:
                    ret[i][j] = min(ret[i][j], ret[i][j - 1] + 1)

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if ret[i][j] == 0 or mat[i][j] == 0:
                    ret[i][j] = 0
                    continue
                if i < m - 1:
                    ret[i][j] = min(ret[i][j], ret[i + 1][j] + 1)
                if j < n - 1:
                    ret[i][j] = min(ret[i][j], ret[i][j + 1] + 1)

        return ret