from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for l in range(m):
            i, j = l, 0
            ini = matrix[i][j]
            while 0 <= i < m and 0 <= j < n:
                if ini != matrix[i][j]:
                    return False
                i += 1
                j += 1

        for l in range(n):
            i, j = 0, l
            ini = matrix[i][j]
            while 0 <= i < m and 0 <= j < n:
                if ini != matrix[i][j]:
                    return False
                i += 1
                j += 1

        return True