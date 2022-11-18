import collections
import functools
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def is_valid(s: str) -> bool:
            c = collections.Counter(s)
            for v in c.values():
                if v != 1:
                    return False
            return True

        def encoding(s: str) -> int:
            res = 0
            for i in range(len(s)):
                res += 1 << (ord(s[i]) - ord("a"))
            return res

        @functools.cache
        def rec(i: int, prefix: int, coding: int) -> int:
            if i == len(arr):
                return prefix

            not_taking = rec(i + 1, prefix, coding)
            taking = 0
            if is_valid(arr[i]):
                cur_coding = encoding(arr[i])
                taking = rec(i + 1, len(arr[i]), cur_coding)
                if cur_coding & coding == 0:
                    taking = max(taking, rec(i + 1, prefix + len(arr[i]), cur_coding | coding))
            return max(not_taking, taking)

        return rec(0, 0, 0)
