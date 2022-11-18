import functools
import math


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @functools.cache
        def dp(idx, last_char, last_char_cnt, k) -> int:
            if k < 0:
                return math.inf
            if idx == len(s):
                return 0

            return min(
                dp(idx + 1, last_char, last_char_cnt, k - 1),
                dp(idx + 1, last_char, last_char_cnt + 1, k) + (last_char_cnt in [1, 9, 99]) if s[idx] == last_char else dp(idx + 1, s[idx], 1, k) + 1)

        return dp(0, "", 0, k)