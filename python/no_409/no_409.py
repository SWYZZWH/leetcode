import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = collections.Counter(s)
        ret = 0
        mid = 0
        for k,v in c.items():
            ret += v - v % 2
            if v % 2 != 0 and mid == 0:
                mid = 1
        return ret + mid