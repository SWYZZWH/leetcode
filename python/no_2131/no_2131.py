import collections
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        c = collections.Counter(words)
        res = 0
        mid = 0
        for k, v in c.items():
            if k[0] == k[1]:
                res += v // 2 * 2
                if not mid:
                    mid += v % 2
            else:
                if k[1] + k[0] not in c:
                    continue
                res += min(c[k[1] + k[0]], c[k])

        return (res + mid) * 2
