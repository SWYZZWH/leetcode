from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.acc = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        s = 0
        for i in range(len(matrix)):
            s += matrix[i][0]
            self.acc[i][0] = s
        s = 0
        for i in range(len(matrix[0])):
            s += matrix[0][i]
            self.acc[0][i] = s

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                self.acc[i][j] = self.acc[i - 1][j] + self.acc[i][j - 1] - self.acc[i - 1][j - 1] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.acc[row2][col2]
        if row1 > 0:
            res -= self.acc[row1 - 1][col2]
        if col1 > 0:
            res -= self.acc[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            res += self.acc[row1 - 1][col1 - 1]
        return res

#     0 1 2
# 2 : 1 2 3
# 1 : 1 2 3
# 0 : 1 2 3
# row1 > row2, col1 < col2

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
