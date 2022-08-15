from typing import List


# visit all col, for each col, binary search row
class Solution:

    # r, c should be valid
    def check(self, mat: List[List[int]], r: int, c: int):
        m, n = len(mat), len(mat[0])
        return (r - 1 < 0 or mat[r - 1][c] < mat[r][c]) and (r + 1 >= m or mat[r + 1][c] < mat[r][c])

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        for i in range(n):
            l, r = 0, m
            while l < r:
                mid = (l + r) // 2
                if self.check(mat, mid, i) and (i - 1 < 0 or mat[mid][i - 1] < mat[mid][i]) and (i + 1 >= n or mat[mid][i + 1] < mat[mid][i]):
                    return [mid, i]
                if mid - 1 < 0 or mat[mid - 1][i] > mat[mid][i]:
                    r = mid
                else:
                    l = mid + 1
