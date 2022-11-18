import collections


class Solution:
    def makeGood(self, s: str) -> str:
        stk = collections.deque()
        for i in range(len(s)):
            if stk and abs(ord(s[i]) - ord(stk[-1])) == 32:
                stk.pop()
                continue
            stk.append(s[i])

        return "".join(stk)