from typing import List


class Solution:
    def max_idx(self, a: int, b: int, c: int) -> int:
        if a >= b and a >= c:
            return 0
        elif b >= a and b >= c:
            return 1
        else:
            return 2

    def min_idx(self, a: int, b: int, c: int) -> int:
        if a <= b and a <= c:
            return 0
        elif b <= a and b <= c:
            return 1
        else:
            return 2

    def mid_idx(self, a: int, b: int, c: int) -> int:
        if b >= a >= c or c >= a >= b:
            return 0
        elif a >= b >= c or c >= b >= a:
            return 1
        else:
            return 2

    # dirty... yet works
    def rec(self, freqs: List[int], strs: List[str]) -> str:
        ret = ""
        while True:
            if freqs[0] == 0 and freqs[1] == 0:
                return ret + strs[2] * (freqs[2] if freqs[2] <= 2 else 2)
            if freqs[1] == 0 and freqs[2] == 0:
                return ret + strs[0] * (freqs[0] if freqs[0] <= 2 else 2)
            if freqs[0] == 0 and freqs[2] == 0:
                return ret + strs[1] * (freqs[1] if freqs[1] <= 2 else 2)
            if freqs[0] == freqs[1] and freqs[1] == freqs[2]:
                return ret + (strs[0] + strs[1] + strs[2]) * freqs[0]
            if freqs[0] == freqs[1] and freqs[1] > freqs[2]:
                return ret + (strs[0] + strs[1]) * (freqs[1] - freqs[2]) + (strs[0] + strs[1] + strs[2]) * freqs[2]
            if freqs[1] == freqs[2] and freqs[1] > freqs[0]:
                return ret + (strs[2] + strs[1]) * (freqs[1] - freqs[0]) + (strs[0] + strs[1] + strs[2]) * freqs[0]
            if freqs[0] == freqs[2] and freqs[0] > freqs[1]:
                return ret + (strs[0] + strs[2]) * (freqs[0] - freqs[1]) + (strs[0] + strs[1] + strs[2]) * freqs[1]
            max_i, mid_i = self.max_idx(freqs[0], freqs[1], freqs[2]), self.mid_idx(freqs[0], freqs[1], freqs[2])
            max_freq = 2 if freqs[max_i] >= 2 else 1
            freqs[max_i] -= max_freq
            freqs[mid_i] -= 1
            ret += strs[max_i] * max_freq + strs[mid_i]

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        return self.rec([a, b, c], ["a", "b", "c"])
