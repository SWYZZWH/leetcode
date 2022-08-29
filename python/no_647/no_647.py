# however, the space complexity can be reduced to O(1)
class Solution:
    # it's clear that the optimized time complexity for this problem is O(n^2)
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        # i, j for left index and right index, s[i:j] is the substring we consider
        dp = [[False for i in range(n + 1)] for j in range(n + 1)]

        ret = 0
        for l in range(n + 1):
            for i in range(n + 1 - l):
                j = i + l
                if l == 0:
                    dp[i][j] = True
                    continue
                if l == 1:
                    dp[i][j] = True
                    ret += 1
                    continue
                if s[i] == s[j - 1] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ret += 1

        return ret


class Solution:
    # O(n^2) solution
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ret = len(s)
        last = [True for i in range(n + 1)]
        dp = [True for i in range(n + 1)]
        for l in range(2, n + 1):
            save = [num for num in dp]
            for i in range(n + 1 - l):
                j = i + l
                if l == 1:
                    dp[i] = True
                    ret += 1
                    continue
                if s[i] == s[j - 1] and last[i + 1]:
                    dp[i] = True
                    ret += 1
                else:
                    dp[i] = False
            last = save
            # print(dp)
        return ret


class Solution:
    # O(n^2) solution, space O(1)
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        ret = 0
        for l in range(n):
            i, j = l, l
            while s[i] == s[j]:
                ret += 1
                if i - 1 >= 0 and j + 1 < n:
                    i -= 1
                    j += 1
                else:
                    break

        for l in range(n - 1):
            i, j = l, l + 1
            while s[i] == s[j]:
                ret += 1
                if i - 1 >= 0 and j + 1 < n:
                    i -= 1
                    j += 1
                else:
                    break

        return ret
