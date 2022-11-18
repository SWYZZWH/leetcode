import math
from typing import List


def minFallingPathSum(self, A):
    for i in range(1, len(A)):
        r = heapq.nsmallest(2, A[i - 1])
        for j in range(len(A[0])):
            A[i][j] += r[1] if A[i - 1][j] == r[0] else r[0]
    return min(A[-1])

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = matrix[0].copy()

        for i in range(1, m):
            tmp = [math.inf for i in range(n)]
            l_min = [math.inf for i in range(n)]
            r_min = [math.inf for i in range(n)]
            for j in range(n):
                l_min[j] = min(l_min[j - 1], dp[j])
            for j in reversed(range(n)):
                r_min[j] = min(r_min[(j + 1) % n], dp[j])
            for j in range(n):
                if j > 0:
                    tmp[j] = min(tmp[j], l_min[j - 1] + matrix[i][j])
                if j < n - 1:
                    tmp[j] = min(tmp[j], r_min[j + 1] + matrix[i][j])
            dp = tmp

        return min(dp)