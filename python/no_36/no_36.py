from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for i in range(9)]
        col_set = [set() for i in range(9)]
        grid_set = [[set() for i in range(3)] for j in range(3)]

        for i in range(9):
            for j in range(9):
                grid_r, grid_c = i // 3, j // 3
                num = board[i][j]
                if num == ".":
                    continue
                if num in row_set[i] or num in col_set[j] or num in grid_set[grid_r][grid_c]:
                    return False
                row_set[i].add(num)
                col_set[j].add(num)
                grid_set[grid_r][grid_c].add(num)

        return True
