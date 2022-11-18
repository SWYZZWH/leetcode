from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ss = set()

        def dfs(s: str, i: int, res: int, prefix: List[str]):
            if res != 0 and i == len(s):
                return
            if res == 0 and i == len(s):
                ss.add(".".join(prefix))
            if res < 0 or i >= len(s):
                return
            if s[i] == "0":
                dfs(s, i + 1, res - 1, prefix + [s[i]])
                return
            for j in range(i, min(i + 3, len(s))):
                if int(s[i: j + 1]) > 255:
                    continue
                dfs(s, j + 1, res - 1, prefix + [s[i: j + 1]])

        dfs(s, 0, 4, [])
        return list(ss)

