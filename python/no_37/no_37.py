from typing import List


class Solution:
    # classic back-tracking
    # with constant space
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # mem = [[set(range(1, 10)) if board[i][j] == "." else {ord(board[i][j]) - ord('0')} for j in range(9)] for i in range(9)]

        def get_candidates(r, c):
            if board[r][c] != '.':
                return {ord(board[r][c]) - ord('0')}

            ret = set(range(1, 10))
            for i in range(9):
                if i == c:
                    continue
                if board[r][i] != '.':
                    num = ord(board[r][i]) - ord('0')
                    if num in ret:
                        ret.remove(num)

            for j in range(9):
                if j == r:
                    continue
                if board[j][c] != '.':
                    num = ord(board[j][c]) - ord('0')
                    if num in ret:
                        ret.remove(num)

            grid_r, grid_c = r // 3, c // 3

            for i in range(3):
                for j in range(3):
                    cur_r, cur_c = grid_r * 3 + i, grid_c * 3 + j
                    if cur_r == r and cur_c == c:
                        continue
                    if board[cur_r][cur_c] != '.':
                        num = ord(board[cur_r][cur_c]) - ord('0')
                        if num in ret:
                            ret.remove(num)

            return ret

        def dfs(i, j) -> bool:
            # print(board)
            if i > 8:
                return True

            cnds = get_candidates(i, j)
            if len(cnds) == 0:
                return False

            nxt_i, nxt_j = i, j + 1
            if j == 8:
                nxt_i += 1
                nxt_j = 0

            cur = board[i][j]
            for cand in cnds:
                board[i][j] = chr(cand + ord("0"))
                if dfs(nxt_i, nxt_j):
                    return True
                board[i][j] = cur

            return False

        dfs(0, 0)

        # print(mem)

        # decided = set()
        #
        # def clear_row(row: int, num: int):
        #     new_decided = set()
        #     for i in range(9):
        #         if len(mem[row][i]) != 1 and num in mem[row][i]:
        #             mem[row][i].remove(num)
        #         if (row, i) not in decided and len(mem[row][i]) == 1:
        #             new_decided.add((row, i))
        #     return new_decided
        #
        # def clear_col(col: int, num: int):
        #     new_decided = set()
        #     for i in range(9):
        #         if len(mem[i][col]) != 1 and num in mem[i][col]:
        #             mem[i][col].remove(num)
        #         if (i, col) not in decided and len(mem[i][col]) == 1:
        #             new_decided.add((i, col))
        #     return new_decided
        #
        # def clear_grid(row: int, col: int, num: int):
        #     new_decided = set()
        #     r_idx, c_idx = row // 3, col // 3
        #     for i in range(3):
        #         for j in range(3):
        #             r, c = r_idx * 3 + i, c_idx * 3 + j
        #             s = mem[r][c]
        #             if len(s) != 1 and num in s:
        #                 s.remove(num)
        #             if (r, c) not in decided and len(s) == 1:
        #                 new_decided.add((r, c))
        #     return new_decided
        #
        # def clear_board():
        #     for i in range(9):
        #         for j in range(9):
        #             if len(mem[i][j]) == 1:
        #                 decided.add((i, j))
        #
        #     q = collections.deque(decided)
        #     while q:
        #         i, j = q.pop()
        #         num = list(mem[i][j])[0]
        #         decided.add((i, j))
        #         for ii, jj in clear_row(i, num):
        #             q.append((ii, jj))
        #             decided.add((ii, jj))
        #         for ii, jj in clear_col(j, num):
        #             q.append((ii, jj))
        #             decided.add((ii, jj))
        #         for ii, jj in clear_grid(i, j, num):
        #             q.append((ii, jj))
        #             decided.add((ii, jj))
        #
        #         board[i][j] = chr(num + ord("0"))
        #         # print(board)
        #
        # clear_board()

        # start trying
        # for i in range(9):
        #     for j in range(9):
    #         if (i, j) not in decided:
