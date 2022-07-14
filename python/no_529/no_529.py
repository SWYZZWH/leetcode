# 529. Minesweeper

# Let's play the minesweeper game (Wikipedia, online game)!
#
# You are given an m x n char matrix board representing the game board where:
#
# 'M' represents an unrevealed mine,
# 'E' represents an unrevealed empty square,
# 'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
# digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
# 'X' represents a revealed mine.
# You are also given an integer array click where click = [clickr, clickc] represents the next click position among all the unrevealed squares ('M' or 'E').
#
# Return the board after revealing this position according to the following rules:
#
# If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
# If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.
# If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
# Return the board when no more squares will be revealed.

# Constraints:
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 50
# board[i][j] is either 'M', 'E', 'B', or a digit from '1' to '8'.
# click.length == 2
# 0 <= clickr < m
# 0 <= clickc < n
# board[clickr][clickc] is either 'M' or 'E'.
from typing import List


# solve recursively
class Solution:
    def findMine(self, board: List[List[str]], i: int, j: int) -> int:
        m, n = len(board), len(board[0])
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'M':
            return 0
        return 1

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        r, c = click[0], click[1]
        if r < 0 or r >= m or c < 0 or c >= n:
            return board
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        if board[r][c] == 'E':
            mineCnt = self.findMine(board, r, c - 1) + self.findMine(board, r, c + 1) + \
                      self.findMine(board, r - 1, c) + self.findMine(board, r - 1, c - 1) + self.findMine(board, r - 1, c + 1) + \
                      self.findMine(board, r + 1, c) + self.findMine(board, r + 1, c - 1) + self.findMine(board, r + 1, c + 1)
            if mineCnt == 0:
                board[r][c] = 'B'
                self.updateBoard(board, [r, c - 1])
                self.updateBoard(board, [r, c + 1])
                self.updateBoard(board, [r - 1, c - 1])
                self.updateBoard(board, [r - 1, c])
                self.updateBoard(board, [r - 1, c + 1])
                self.updateBoard(board, [r + 1, c - 1])
                self.updateBoard(board, [r + 1, c])
                self.updateBoard(board, [r + 1, c + 1])
            else:
                board[r][c] = chr(ord('0') + mineCnt)
        return board
