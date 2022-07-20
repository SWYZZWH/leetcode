# 48. Rotate Image
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
from typing import List


class Solution:
    # basic linear algebra
    # first flip by the line: y = n - x
    # then flip by the line x = mid
    # i, j -> n - j, n - i
    # let i1 = n - j, j1 = n - i
    # then i1, j1 -> i1, n - j1
    # so, final_pos = (i1, n - j1) = (n - j , n - (n - i)) = (n - j, i)
    # (i, j) -> (n - j, i)
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(0, i):
                matrix[i][j], matrix[n - j - 1][n - i - 1] = matrix[n - j - 1][n - i - 1], matrix[i][j]
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
