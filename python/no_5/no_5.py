# top-down will lead to time exceeding
class Solution:
    def __init__(self):
        self.dp = {}
        self.max_len = 0
        self.ret = ""

    def rec(self, s, i, j):
        if (i, j) in self.dp:
            return

        is_palindrom = False

        if i == j:
            is_palindrom = True
        elif j == i + 1:
            is_palindrom = s[i] == s[j]
        else:
            is_palindrom = s[i] == s[j] and self.rec(s, i + 1, j - 1)

        if is_palindrom:
            self.dp[(i, j)] = is_palindrom
            if j - i + 1 > self.max_len:
                self.max_len = j - i + 1
                self.ret = s[i:j + 1]
        return is_palindrom

    def longestPalindrome(self, s: str) -> str:
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                self.rec(s, i, j)
        return self.ret

