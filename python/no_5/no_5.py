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


# the idea of expanding from center is elegant


# discuss by odd and even
class Solution:
    def longestPalindrome(self, s: str) -> str:
        left, right = 0, -1
        for i in range(len(s)):
            # odd
            l, r = i, i
            while l - 1 >= 0 and r + 1 < len(s) and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1
            if r - l > right - left:
                left = l
                right = r

            # even
            l, r = i, i - 1
            while l - 1 >= 0 and r + 1 < len(s) and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1
            if r - l > right - left:
                left = l
                right = r

        return s[left: right + 1]


# avoid discussing odd and even
class Solution:
    def longestPalindrome(self, s: str) -> str:
        left, right = 0, -1
        for i in range(len(s)):
            r = i
            while r + 1 < len(s) and s[r] == s[r + 1]:
                r += 1

            l = i
            while l - 1 >= 0 and r + 1 < len(s) and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1

            if r - l > right - left:
                left = l
                right = r

        return s[left: right + 1]
