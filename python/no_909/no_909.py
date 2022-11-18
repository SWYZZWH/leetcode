from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get_index(num: int) -> (int, int):
            n = len(board)
            row_idx = n - ((num - 1) // n) - 1
            col_idx = (num - 1) % n if (n - row_idx - 1) % 2 == 0 else (n - (num - 1) % n - 1)
            return row_idx, col_idx

        if n == 1:
            return 0
        q = deque([1])
        seen = {1}
        steps = 0
        while q:
            tmp = deque()
            while q:
                e = q.popleft()
                for i in range(1, 7):
                    if e + i == n * n:
                        return steps + 1
                    r, c = get_index(e + i)
                    if board[r][c] == -1:
                        if e + i not in seen:
                            seen.add(e + i)
                            tmp.append(e + i)
                    else:
                        # notice, we haven't seen e + i in this branch!
                        if board[r][c] == n * n:
                            return steps + 1
                        if board[r][c] not in seen:
                            tmp.append(board[r][c])
                            seen.add(board[r][c])

            q = tmp
            steps += 1

        return -1