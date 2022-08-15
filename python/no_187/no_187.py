import collections
from typing import List


class Solution:
    # simple dict and sliding window, L can be extend to any int
    # this solution is reaching O((n-L)L) complexity
    # cause it takes L for calculate hash for a L length string

    # we can use rolling hash for O(n-L) complexity
    # or we can use bit mask
    # def findRepeatedDnaSequences(self, s: str) -> List[str]:
    #     d = collections.defaultdict(int)
    #     for i in range(0, len(s) - 9):
    #         d[s[i:i + 10]] += 1
    #     print(d)
    #     ret = []
    #     for k, v in d.items():
    #         if v > 1:
    #             ret.append(k)
    #     return ret

    def dna2int(self, c) -> int:
        if c == 'A':
            return 0
        if c == 'C':
            return 1
        if c == 'G':
            return 2
        else:
            return 3

    def int2dna(self, i: int) -> str:
        if i == 0:
            return "A"
        if i == 1:
            return "C"
        if i == 2:
            return "G"
        else:
            return "T"

    def h2str(self, h: int, l: int) -> str:
        s = ["" for i in range(l)]
        for i in range(l):
            s[l - i - 1] = self.int2dna(h % 4)
            h //= 4
        return "".join(s)

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        d = collections.defaultdict(int)
        h = 0
        for i in range(0, 10):
            h *= 4
            h += self.dna2int(s[i])
        d[h] += 1

        for i in range(1, len(s) - 9):
            h -= self.dna2int(s[i - 1]) * (4 ** 9)
            h *= 4
            h += self.dna2int(s[i + 9])
            d[h] += 1

        ret = []
        for k, v in d.items():
            if v > 1:
                ret.append(self.h2str(k, 10))

        return ret
