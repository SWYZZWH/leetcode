from typing import List


class Solution:
    # dfs + back-tracking
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ret = []
        if n == 0:
            return ret

        def dfs(n: int, i: int, prefix: str):
            if i == n:
                ret.append(int(prefix))
                return
            for j in range(10):
                if abs(ord(prefix[-1]) - ord("0") - j) != k:
                    continue
                dfs(n, i + 1, prefix + str(j))

        for j in range(1, 10):
            dfs(n, 1, str(j))
        return ret