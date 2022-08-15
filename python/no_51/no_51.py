# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other.
#
#  Given an integer n, return all distinct solutions to the n-queens puzzle.
# You may return the answer in any order.
#
#  Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
#
#
#  Example 1:
#
#
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as
# shown above
#
#
#  Example 2:
#
#
# Input: n = 1
# Output: [["Q"]]
#
#
#
#  Constraints:
#
#
#  1 <= n <= 9
#
#
#  Related Topics Array Backtracking 👍 7654 👎 183


# leetcode submit region begin(Prohibit modification and deletion)

# classic dfs
from typing import List


class Solution:
    # def check(self, board: List[List[str]], i: int, j: int) -> bool:
    #     left, mid, right = j, j, j
    #     while i > 0:
    #         i -= 1
    #         left -= 1
    #         right += 1
    #         if left >= 0 and board[i][left] == "Q":
    #             return False
    #         if right < len(board) and board[i][right] == "Q":
    #             return False
    #         if board[i][mid] == "Q":
    #             return False
    #     return True
    #
    # def dfs(self, board: List[List[str]], i: int, ret_set: List[List[str]]):
    #     if i == len(board):
    #         ret_set.append(["".join(lst) for lst in board])
    #         return
    #     for j in range(len(board)):
    #         if self.check(board, i, j):
    #             board[i][j] = "Q"
    #             self.dfs(board, i + 1, ret_set)
    #             board[i][j] = "."
    #
    # def solveNQueens(self, n: int) -> List[List[str]]:
    #     ret = []
    #     self.dfs([["." for i in range(n)] for j in range(n)], 0, ret)
    #     return ret

    # set optimization
    def dfs(self, board: List[List[str]], col_set, diamond_set1, diamond_set2, i: int, ret_set: List[List[str]]):
        if i == len(board):
            ret_set.append(["".join(lst) for lst in board])
            return
        for j in range(len(board)):
            if j in col_set or j - i in diamond_set1 or i + j in diamond_set2:
                continue
            board[i][j] = "Q"
            col_set.add(j)
            diamond_set1.add(j - i)
            diamond_set2.add(i + j)
            self.dfs(board, col_set, diamond_set1, diamond_set2, i + 1, ret_set)
            col_set.remove(j)
            diamond_set1.remove(j - i)
            diamond_set2.remove(i + j)
            board[i][j] = "."

    def solveNQueens(self, n: int) -> List[List[str]]:
        ret = []
        col_set, diamond_set1, diamond_set2 = set(), set(), set()
        self.dfs([["." for i in range(n)] for j in range(n)], col_set, diamond_set1, diamond_set2, 0, ret)
        return ret


# leetcode submit region end(Prohibit modification and deletion)
