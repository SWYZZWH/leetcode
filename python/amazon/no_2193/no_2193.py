class Solution:
    # notice: adjacent
    # first consider the outer characters s[-1], l, r = 0, len(s) - 1
    # if s[-1] only shows up once, then it takes n / 2 steps, r -= 1
    # for s[r], find the first s[l] == s[r], takes
    def minMovesToMakePalindrome(self, s: str) -> int:
        res = 0
        s = list(s)
        while s:
            l = 0
            while s[l] != s[-1]:
                l += 1
            if l == len(s) - 1:
                mid = (len(s) - 1) // 2
                res += mid
                s.pop(-1)
            else:
                res += l
                s.pop(l)
                s.pop(-1)
        return res