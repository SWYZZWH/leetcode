from typing import List


class Solution:
    # arts of parenthesis
    def removeInvalidParentheses(self, s: str) -> List[str]:
        levels = 0
        right_removals = 0
        for i in range(len(s)):
            if s[i] == "(":
                levels += 1
            elif s[i] == ")":
                if levels == 0:
                    right_removals += 1
                else:
                    levels -= 1
        left_removals = levels

        ss = set()

        def dfs(i: int, l: int, r: int, l_rem: int, r_rem: int, prefix: str):
            if l_rem < 0 or r_rem < 0:
                return
            if r > l:
                return
            if i == len(s):
                if l_rem == 0 and r_rem == 0 and l == r:
                    ss.add(prefix)
                return

            if s[i] == "(":
                if l_rem:
                    dfs(i + 1, l, r, l_rem - 1, r_rem, prefix)
                dfs(i + 1, l + 1, r, l_rem, r_rem, prefix + "(")
            elif s[i] == ")":
                if r_rem:
                    dfs(i + 1, l, r, l_rem, r_rem - 1, prefix)
                dfs(i + 1, l, r + 1, l_rem, r_rem, prefix + ")")
            else:
                dfs(i + 1, l, r, l_rem, r_rem, prefix + s[i])

        dfs(0, 0, 0, left_removals, right_removals, "")
        return list(ss)