from typing import List


class Solution:
    visited = 999

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ret = []
        i, j = 0, 0
        while True:
            # notice: python slice is always reference
            cur = len(ret)
            if m > i >= 0 and n > j >= 0 and matrix[i][j] != self.visited:
                ret.append(matrix[i][j])
                matrix[i][j] = self.visited
            while j + 1 < n and matrix[i][j + 1] != self.visited:
                j += 1
                ret.append(matrix[i][j])
                matrix[i][j] = self.visited
            while i + 1 < m and matrix[i + 1][j] != self.visited:
                i += 1
                ret.append(matrix[i][j])
                matrix[i][j] = self.visited
            while j - 1 >= 0 and matrix[i][j - 1] != self.visited:
                j -= 1
                ret.append(matrix[i][j])
                matrix[i][j] = self.visited
            while i - 1 >= 0 and matrix[i - 1][j] != self.visited:
                i -= 1
                ret.append(matrix[i][j])
                matrix[i][j] = self.visited
            if cur == len(ret):
                return ret
